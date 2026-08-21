from manim import *
import numpy as np
from scipy.special import sph_harm_y
from functools import lru_cache


HARMONICS = [
    (0, 0),
    (1, 0),
    (2, 0),
    (2, 2),
    (3, 2),
    (5, 2),
]

SURFACE_SCALE = 2.3
SURFACE_RESOLUTION = (32, 64)

DISPLAY_TIME = 1.2
TRANSITION_TIME = 0.9


def real_spherical_harmonic(l, m, theta, phi):
    """
    Real-valued spherical harmonic using SciPy's convention:
      theta = polar / colatitude angle
      phi   = azimuthal angle
    """

    ylm = sph_harm_y(l, abs(m), theta, phi)

    if m > 0:
        return np.sqrt(2) * (-1) ** m * np.real(ylm)

    if m < 0:
        return np.sqrt(2) * (-1) ** m * np.imag(ylm)

    return np.real(ylm)


@lru_cache(maxsize=None)
def harmonic_normalization(l, m):
    """
    Compute max |Y_lm| once per harmonic.
    """

    theta = np.linspace(0, np.pi, 160)
    phi = np.linspace(0, 2 * np.pi, 320)

    theta_grid, phi_grid = np.meshgrid(
        theta,
        phi,
        indexing="ij",
    )

    values = real_spherical_harmonic(
        l,
        m,
        theta_grid,
        phi_grid,
    )

    return float(np.max(np.abs(values)))


def harmonic_point(l, m, theta, phi):
    """
    Use |Y_lm| as a radial displacement to produce the
    familiar spherical-harmonic lobe visualization.
    """

    value = real_spherical_harmonic(
        l,
        m,
        theta,
        phi,
    )

    norm = harmonic_normalization(l, m)

    radius = SURFACE_SCALE * abs(value) / norm

    # Small offset keeps nodal regions from collapsing completely.
    radius += 0.035

    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)

    return np.array([x, y, z])


def make_harmonic_surface(l, m):
    return Surface(
        lambda theta, phi: harmonic_point(
            l,
            m,
            theta,
            phi,
        ),
        u_range=[0.001, PI - 0.001],
        v_range=[0, TAU],
        resolution=SURFACE_RESOLUTION,
        fill_opacity=0.92,
        checkerboard_colors=[
            BLUE_D,
            BLUE_E,
        ],
        stroke_width=0.1,
        stroke_color=BLUE_A,
    )


def make_label(l, m):
    harmonic = MathTex(
        rf"Y_{{{l}}}^{{{m}}}",
        font_size=52,
    )

    values = MathTex(
        rf"\ell={l},\qquad m={m}",
        font_size=28,
        color=GRAY_B,
    )

    group = VGroup(
        harmonic,
        values,
    ).arrange(
        DOWN,
        buff=0.12,
    )

    group.to_edge(DOWN)

    return group


class SphericalHarmonicsIntro(ThreeDScene):

    def construct(self):

        # Camera
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-35 * DEGREES,
            zoom=1.1,
        )

        self.begin_ambient_camera_rotation(
            rate=0.10
        )

        # Header
        title = Text(
            "Spherical Harmonics",
            font_size=42,
            weight=MEDIUM,
        )

        subtitle = Text(
            "A basis for describing structure on a sphere",
            font_size=22,
            color=GRAY_B,
        )

        header = VGroup(
            title,
            subtitle,
        ).arrange(
            DOWN,
            buff=0.12,
        )

        header.to_edge(UP)

        self.add_fixed_in_frame_mobjects(header)

        self.play(
            FadeIn(header),
            run_time=0.8,
        )

        # Initial harmonic
        l, m = HARMONICS[0]

        surface = make_harmonic_surface(l, m)
        label = make_label(l, m)

        self.add_fixed_in_frame_mobjects(label)

        self.play(
            FadeIn(surface),
            FadeIn(label),
            run_time=1,
        )

        self.wait(DISPLAY_TIME)

        # Cycle through harmonics
        for new_l, new_m in HARMONICS[1:]:

            new_surface = make_harmonic_surface(
                new_l,
                new_m,
            )

            new_label = make_label(
                new_l,
                new_m,
            )

            self.add_fixed_in_frame_mobjects(
                new_label
            )

            self.play(
                Transform(
                    surface,
                    new_surface,
                ),
                FadeOut(label),
                FadeIn(new_label),
                run_time=TRANSITION_TIME,
            )

            label = new_label

            self.wait(DISPLAY_TIME)

        # Final explanation
        closing = Text(
            "Higher degree ℓ allows finer angular structure",
            font_size=25,
            color=GRAY_B,
        )

        closing.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(
            closing
        )

        self.play(
            FadeOut(label),
            FadeIn(closing),
            run_time=0.6,
        )

        self.wait(2)

        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(surface),
            FadeOut(header),
            FadeOut(closing),
            run_time=1,
        )