import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import update_vgc_meta as updater


REPORT = """Total battles: 12,345
Avg. weight/team: 0.315
| Rank | Pokemon | Usage % | Raw | % | Real | % |
| 1 | Kingambit | 62.50281% | 34069 | 44.304% | 16267 | 45.824% |
| 2 | Sneasler | 36.87580% | 25366 | 32.987% | 14150 | 39.861% |
"""


def snapshot(month, regulation, pokemon):
    return {
        "month": month,
        "regulation": regulation,
        "pokemon": pokemon,
    }


class ParseReportTests(unittest.TestCase):
    def test_parses_report_summary_and_all_usage_columns(self):
        battles, weight, rows = updater.parse_report(REPORT)
        self.assertEqual(battles, 12345)
        self.assertEqual(weight, 0.315)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["rank"], 1)
        self.assertEqual(rows[0]["name"], "Kingambit")
        self.assertEqual(rows[0]["usage_pct"], 62.50281)
        self.assertEqual(rows[0]["raw"], 34069)
        self.assertEqual(rows[0]["real_pct"], 45.824)

    def test_rejects_incomplete_or_invalid_reports(self):
        with self.assertRaisesRegex(ValueError, "missing its battle"):
            updater.parse_report("| 1 | Pikachu | 1.0% | 1 | 1.0% | 1 | 1.0% |")
        duplicate = REPORT + "| 3 | Kingambit | 1.0% | 1 | 1.0% | 1 | 1.0% |\n"
        with self.assertRaisesRegex(ValueError, "Duplicate Pokémon"):
            updater.parse_report(duplicate)


class ComparisonTests(unittest.TestCase):
    def test_union_comparison_calculates_percentage_points_and_rank_movement(self):
        august = snapshot(
            "2026-08",
            "M-B",
            [
                {"name": "A", "rank": 1, "usage_pct": 60.0},
                {"name": "B", "rank": 2, "usage_pct": 30.0},
            ],
        )
        september = snapshot(
            "2026-09",
            "M-B",
            [
                {"name": "B", "rank": 1, "usage_pct": 50.0},
                {"name": "C", "rank": 2, "usage_pct": 25.0},
            ],
        )
        rows = updater.build_comparison_rows([august, september])
        by_name = {row["pokemon"]: row for row in rows}
        self.assertEqual(len(rows), 3)
        self.assertEqual(by_name["B"]["usage_change_pp"], 20.0)
        self.assertEqual(by_name["B"]["rank_movement"], 1)
        self.assertEqual(by_name["A"]["coverage"], "earlier only")
        self.assertEqual(by_name["C"]["coverage"], "later only")
        self.assertIsNone(by_name["A"]["usage_change_pp"])

    def test_does_not_compare_across_regulations(self):
        report_a = snapshot("2026-08", "M-A", [{"name": "A", "rank": 1, "usage_pct": 20.0}])
        report_b = snapshot("2026-09", "M-B", [{"name": "A", "rank": 1, "usage_pct": 20.0}])
        self.assertEqual(updater.build_comparison_rows([report_a, report_b]), [])

    def test_spearman_is_calculated_on_reindexed_shared_species(self):
        august = snapshot(
            "2026-08",
            "M-B",
            [
                {"name": "A", "rank": 1, "usage_pct": 40.0},
                {"name": "B", "rank": 2, "usage_pct": 35.0},
                {"name": "C", "rank": 3, "usage_pct": 25.0},
            ],
        )
        september = snapshot(
            "2026-09",
            "M-B",
            [
                {"name": "B", "rank": 1, "usage_pct": 40.0},
                {"name": "A", "rank": 2, "usage_pct": 35.0},
                {"name": "C", "rank": 3, "usage_pct": 25.0},
            ],
        )
        august["total_battles"] = 100
        september["total_battles"] = 80
        result = updater.summarize_adjacent_pairs([august, september], top_n=2)[0]
        self.assertEqual(result["shared_roster"], 3)
        self.assertEqual(result["sum_squared_rank_differences"], 2)
        self.assertAlmostEqual(result["spearman_rho_shared"], 0.5)
        self.assertEqual(result["top_n_overlap"], 2)
        self.assertEqual(result["earlier_battles"], 100)


class RetiredSnapshotCleanupTests(unittest.TestCase):
    def test_cleanup_is_scoped_to_retired_source_directory(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            snapshots_dir = Path(temporary_directory)
            retired_file = snapshots_dir / "Doubles" / "Current" / "old.json"
            smogon_file = snapshots_dir / "Doubles-Bo3" / "M-B" / "2026-09.json"
            other_source_file = snapshots_dir / "Other" / "snapshot.json"
            malformed_file = snapshots_dir / "Other" / "broken.json"
            for path in (retired_file, smogon_file, other_source_file, malformed_file):
                path.parent.mkdir(parents=True, exist_ok=True)
            retired_file.write_text('{"source": "retired"}', encoding="utf-8")
            smogon_file.write_text('{"source": "Smogon / Pokémon Showdown"}', encoding="utf-8")
            other_source_file.write_text('{"source": "another provider"}', encoding="utf-8")
            malformed_file.write_text("not json", encoding="utf-8")

            updater.remove_retired_snapshots(snapshots_dir)

            self.assertFalse(retired_file.exists())
            self.assertTrue(smogon_file.exists())
            self.assertTrue(other_source_file.exists())
            self.assertTrue(malformed_file.exists())


if __name__ == "__main__":
    unittest.main()
