-- Compare Smogon Champions VGC Bo3 usage reports at the same 1630 cutoff.
-- Usage change is measured in percentage points; positive rank movement means a climb.
WITH
aug AS (
    SELECT
        u.pokemon,
        u.source_rank AS aug_rank,
        u.usage_pct AS aug_usage_pct
    FROM monthly_reports AS r
    JOIN pokemon_usage AS u USING (report_id)
    WHERE r.month = '2026-08'
      AND r.regulation = 'M-B'
      AND r.format = 'Bo3'
      AND r.rating_cutoff = 1630
),
sep AS (
    SELECT
        u.pokemon,
        u.source_rank AS sep_rank,
        u.usage_pct AS sep_usage_pct
    FROM monthly_reports AS r
    JOIN pokemon_usage AS u USING (report_id)
    WHERE r.month = '2026-09'
      AND r.regulation = 'M-B'
      AND r.format = 'Bo3'
      AND r.rating_cutoff = 1630
),
roster AS (
    SELECT pokemon FROM aug
    UNION
    SELECT pokemon FROM sep
)
SELECT
    roster.pokemon,
    CASE
        WHEN aug.pokemon IS NOT NULL AND sep.pokemon IS NOT NULL THEN 'both months'
        WHEN aug.pokemon IS NOT NULL THEN 'August only'
        ELSE 'September only'
    END AS coverage,
    aug.aug_rank,
    sep.sep_rank,
    aug.aug_usage_pct,
    sep.sep_usage_pct,
    ROUND(sep.sep_usage_pct - aug.aug_usage_pct, 5) AS usage_change_pp,
    aug.aug_rank - sep.sep_rank AS rank_movement
FROM roster
LEFT JOIN aug USING (pokemon)
LEFT JOIN sep USING (pokemon)
ORDER BY
    CASE coverage WHEN 'both months' THEN 0 WHEN 'August only' THEN 1 ELSE 2 END,
    usage_change_pp DESC,
    roster.pokemon;
