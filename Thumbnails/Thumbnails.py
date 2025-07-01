from manim import *
from manim_physics import *
from scipy.integrate import quad
import math

# config.background_color = "#00001a"
Last = 0


class Fourier(VectorScene):
    def construct(self):

        title = (
            Tex(
                r"""Fourier Analysis""",
            )
            .scale(3)
            .set_color_by_gradient(TEAL, WHITE)
            .to_edge(UP, buff=1.1)
        )
        self.add(NumberPlane())
        self.add(StandingWave(4, 8).set_stroke(width=5))
        A = np.array([-5, -3, 0])
        B = np.array([-1, -3, 0])
        C = np.array([-5, -1, 0])
        triangle = Polygon(A, B, C, fill_color=BLUE, fill_opacity=0.5)
        eq = (
            MathTex(
                r"""X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt""",
                color=TEAL_A,
            )
            .scale(1)
            .to_corner(DR, buff=1)
        )
        self.add(triangle)
        self.add(title)
        self.add(eq)
        self.wait(5)


class Linearity(VectorScene):
    def construct(self):

        plane = NumberPlane()
        title = (
            Tex(
                r"""Linear Differential\\ Equations""",
            )
            .scale(3)
            .set_color_by_gradient(ORANGE, PURPLE)
            .to_edge(UP, buff=1.1)
        )
        self.add(plane)
        eq = (
            MathTex(
                r"""L(y(x))=b(x)""",
                color=PURPLE_A,
            )
            .scale(1)
            .to_corner(DR, buff=1.2)
        )
        eq1 = (
            MathTex(
                r"""L(af+bg)=aL(f)+bL(g)""",
                color=ORANGE,
            )
            .scale(1)
            .to_corner(DL, buff=0.8)
        )
        graph1 = plane.plot(lambda x: -0.5 * x - 2, color=ORANGE, stroke_width=7)
        graph2 = plane.plot(lambda x: x - 4.9, color=PURPLE, stroke_width=7)
        graph3 = plane.plot(
            lambda x: -0.5 * x - 2.7,
            stroke_width=7,
            stroke_color=color_gradient([ORANGE, PURPLE], 10),
        )
        self.add(title)
        self.add(eq)
        self.add(eq1)
        self.add(graph1)
        self.add(graph2)
        self.add(graph3)


class RootLocus(VectorScene):
    def construct(self):

        plane = NumberPlane()
        title = (
            Tex(
                r"""Root Locus\\ Analysis""",
            )
            .scale(3)
            .set_color_by_gradient(YELLOW, WHITE)
            .to_edge(UP, buff=1.1)
        )
        self.add(plane)
        eq = (
            MathTex(
                r"""\mathcal{L}\left\{ f \right\}(s)=\int_{0}^{\infty}f(t)e^{-st}dt""",
                color=YELLOW,
            )
            .scale(1)
            .to_edge(RIGHT, buff=0.5)
            .shift(DOWN * 0.9)
        )
        eq1 = (
            MathTex(
                r"""s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}""",
                color=WHITE,
            )
            .scale(1)
            .to_edge(LEFT, buff=0.5)
            .to_edge(DOWN, buff=2.2)
        )

        D = [1, 9, 29, 55, 50]
        poles = [[z.real, z.imag, 1] for z in np.roots(D)]

        N = [0, 1, 7, 24, 18]
        zeros = [[z.real, z.imag, 1] for z in np.roots(N)]

        def ceqf(k):
            ceq = []
            for i in range(len(D)):
                p = D[i]
                z = N[i]
                ceq.append(p + z * k)
            return ceq

        root_locus1 = ParametricFunction(
            lambda t: [
                np.roots(ceqf(t))[2].real,
                np.roots(ceqf(t))[2].imag,
                1,
            ],
            t_range=[0, 60],
            color=YELLOW,
            stroke_width=6,
        )
        root_locus2 = ParametricFunction(
            lambda t: [
                np.roots(ceqf(t))[0].real,
                np.roots(ceqf(t))[0].imag,
                1,
            ],
            t_range=[0, 60],
            color=YELLOW,
            stroke_width=6,
        )
        axis = Axes(
            x_length=4,
            y_length=3,
            tips=False,
            axis_config={"include_ticks": False, "stroke_opacity": 0},
            x_range=[0, 5],
            y_range=[-1.5, 1.5],
        ).move_to([4, -2.5, 10])
        response = axis.plot(
            lambda x: math.exp(-0.5 * x) * math.cos(10 * x), x_range=[0, 5]
        )
        pole1 = Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(poles[2])
        pole2 = Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(poles[0])
        zero1 = Circle(radius=0.1, color=YELLOW, stroke_width=6).move_to(zeros[1])
        self.add(title)
        self.add(eq)
        self.add(eq1)
        self.add(root_locus1)
        self.add(root_locus2)
        self.add(pole1)
        self.add(pole2)
        self.add(zero1)
        self.add(response)

class DrawLocus(VectorScene):
    def construct(self):

        plane = NumberPlane()
        self.add(plane)
        system = (
            MathTex("G(s)H(s)=", "K", r"\frac{s+2}{s^2+s}")
            .scale(0.7)
            .to_corner(UR, buff=1.1)
        )
        system[1].set_color(YELLOW)
        self.play(Write(system))

        D = [1,1,0]
        poles = [[z.real, z.imag, 1] for z in np.roots(D)]

        N = [0,1,2]
        zeros = [[z.real, z.imag, 1] for z in np.roots(N)]

        for pole in poles:
            self.play(
                Create(Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(pole))
            )
            self.wait(1)

        for zero in zeros:
            self.play(
                Create(Circle(radius=0.1, color=YELLOW, stroke_width=6).move_to(zero))
            )
            self.wait(1)

        def ceqf(k):
            ceq = []
            for i in range(len(D)):
                p = D[i]
                z = N[i]
                ceq.append(p + z * k)
            return ceq

        K = ValueTracker(0)

        root_loci = []
        for i in range(len(poles)):
            root_locus = always_redraw(
                lambda: ParametricFunction(
                    lambda t: [
                        np.roots(ceqf(t))[i].real,
                        np.roots(ceqf(t))[i].imag,
                        1,
                    ],
                    t_range=[0, 60],
                    color=YELLOW,
                    stroke_width=6,
                )
            )
            root_loci.append(root_locus)
        for root in root_loci:
            self.add(root)
        #self.play(K.animate.set_value(60))
        self.wait(2)
