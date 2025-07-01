from manim import *
from manim_physics import *
import math

Skip =0


class Root(Scene):

    def construct(self):

        self.next_section(skip_animations=Skip)

        # Tracker variable
        p = ValueTracker(0.5)

        # Create a mass (a rectangle)
        mass_block = always_redraw(
            lambda: RoundedRectangle(
                height=2, width=4, color=BLUE, fill_opacity=1, corner_radius=0.25
            ).shift(UP * p.get_value())
        )
        mass_label = always_redraw(
            lambda: MathTex("m", color=BLUE_A).scale(2).move_to(mass_block)
        )
        mass = VGroup(mass_block, mass_label)

        # Create ground
        ground = Line(start=[-3, -3, 0], end=[3, -3, 0])

        # Create a damper
        damper_stick = Line(start=[0.75, -3, 0], end=[0.75, -1.6, 0])
        damper_plate = Line(start=[0.75 - 0.34, -1.6, 0], end=[0.75 + 0.34, -1.6, 0])
        damper_box1 = always_redraw(
            lambda: Line(
                start=[0.75 - 0.4, mass.get_bottom()[1] - 0.3, 0],
                end=[0.75 + 0.4, mass.get_bottom()[1] - 0.3, 0],
                color=GREEN,
            )
        )
        damper_box2 = always_redraw(
            lambda: Line(
                start=[0.75 - 0.4, mass.get_bottom()[1] - 1.4 - 0.3, 0],
                end=[0.75 - 0.4, mass.get_bottom()[1] - 0.3, 0],
                color=GREEN,
            )
        )
        damper_box3 = always_redraw(
            lambda: Line(
                start=[0.75 + 0.4, mass.get_bottom()[1] - 1.4 - 0.3, 0],
                end=[0.75 + 0.4, mass.get_bottom()[1] - 0.3, 0],
                color=GREEN,
            )
        )
        damper_extension = always_redraw(
            lambda: Line(
                start=[0.75, mass.get_bottom()[1] - 0.3, 0],
                end=[0.75, mass.get_bottom()[1], 0],
                color=GREEN,
            )
        )
        damper = VGroup(
            damper_stick,
            damper_plate,
            damper_box1,
            damper_box2,
            damper_box3,
            damper_extension,
        )
        damper.set_color(GREEN)

        # Create a spring using ParametricFunction
        a = 0.5
        spring = always_redraw(
            lambda: ParametricFunction(
                lambda t: [
                    (2 * a / PI)
                    * math.asin(
                        math.sin(2 * PI / ((mass.get_bottom()[1] - (-3)) / 4) * t)
                    ),
                    t,
                    0,
                ],
                t_range=[0, 4 * ((mass.get_bottom()[1] - (-3)) / 4)],
                color=YELLOW,
            )
            .next_to(mass, DOWN, buff=0)
            .shift(LEFT * 0.75)
        )

        # Create a variable x
        x_start = Line(start=[4, -0.2, 0], end=[4.5, -0.2, 0])
        x_track = always_redraw(
            lambda: Line(
                start=[4.25, -0.2, 0], end=[4.25, mass.get_center()[1] + 1, 0]
            ).add_tip()
        )
        x_label = always_redraw(lambda: MathTex("y").scale(2).next_to(x_track, RIGHT))
        x = VGroup(x_start, x_track, x_label)

        # Add mass and spring to the scene
        self.add(mass, spring, ground, damper, x)

        # Animate the mass and spring
        for i in range(0, 7, 2):
            self.play(p.animate.set_value(1.2 - i * 0.1), run_time=0.75)
            self.play(p.animate.set_value(-0.2 + i * 0.1), run_time=0.75)
        self.wait(1)

        # Equation of motion
        eq1 = MathTex(r"""\Sigma F=-""", "k", "y").to_edge(UP, buff=1).scale(1.5)
        eq1[1].set_color(YELLOW)
        self.play(Write(eq1))
        self.wait(2)
        eq2 = (
            MathTex(r"""\Sigma F=-""", "k", "y", "-", "b", r"""\dot y""")
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq2[1].set_color(YELLOW)
        eq2[4].set_color(GREEN)
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait(2)
        eq3 = (
            MathTex(
                r"""\Sigma F=-""",
                "k",
                "y",
                "-",
                "b",
                r"""\dot y""",
                r"""+F_{\text{external}}""",
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq3[1].set_color(YELLOW)
        eq3[4].set_color(GREEN)
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait(2)
        eq4 = (
            MathTex(
                r"""\Sigma F=-""",
                "k",
                "y",
                "-",
                "b",
                r"""\dot y""",
                r"""+F_{\text{external}}""",
                "=",
                "m",
                r"""\ddot y""",
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq4[1].set_color(YELLOW)
        eq4[4].set_color(GREEN)
        eq4[8].set_color(BLUE)
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait(2)
        eq5 = (
            MathTex(
                "m",
                r"""\ddot y+""",
                "b",
                r"""\dot y+""",
                "k",
                r"""y=F_{\text{external}}""",
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq5[0].set_color(BLUE)
        eq5[2].set_color(GREEN)
        eq5[4].set_color(YELLOW)
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        eq6 = (
            MathTex(
                r"""\ddot y+\frac{b}{m}\dot y+\frac{k}{m} y=\frac{F_{\text{external}}}{m}"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        self.play(
            TransformMatchingShapes(eq5, eq6),
            FadeOut(VGroup(mass, spring, ground, damper, x)),
        )
        self.wait(1)
        eq7 = (
            MathTex(
                r"""\ddot y+\frac{b}{m}\dot y+\left( \sqrt{\frac{k}{m}} \right)^2 y=\left( 
                \sqrt{\frac{k}{m}} \right)^2\frac{F_{\text{external}}}{k}"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(eq6, eq7))
        self.wait(1)
        eq8 = (
            MathTex(
                r"""\ddot y+\frac{b}{m}\dot y+\omega_n^2 y=\omega_n^2\frac{F_{\text{external}}}{k}"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq9 = (
            MathTex(r"""\omega_n=\sqrt{\frac{k}{m}}""")
            .to_edge(UP, buff=4)
            .to_edge(LEFT, buff=3)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(eq7, eq8), Write(eq9))
        self.wait(1)
        eq10 = (
            MathTex(
                r"""\ddot y+2\zeta\omega_n\dot y+\omega_n^2 y=\omega_n^2\frac{F_{\text{external}}}{k}"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        eq11 = (
            MathTex(r"""\zeta=\frac{b}{2m\omega_n}""")
            .to_edge(UP, buff=4.2)
            .to_edge(RIGHT, buff=3)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(eq8, eq10), Write(eq11))
        self.wait(1)
        eq12 = (
            MathTex(r"""\ddot y+2\zeta\omega_n\dot y+\omega_n^2 y=0""")
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(eq10, eq12))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(FadeOut(VGroup(eq9, eq11, eq12)))
        eq13 = (
            Title(
                r"""\textbf{Linear Time-Invariant System}""",
                color=YELLOW,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(Write(eq13))
        eq14 = (
            Tex(
                r"""A system that produces an output signal from any input signal\\subject to 
                the constraints of linearity and time-invariance"""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        self.play(Write(eq14))
        rec = Rectangle(height=2, width=4, color=YELLOW).shift(DOWN * 0.5)
        rec_label = Tex("LTI System").move_to(rec)
        in_arrow = Line(start=[-4, -0.5, 0], end=[-2, -0.5, 0]).add_tip()
        out_arrow = Line(start=[2, -0.5, 0], end=[4, -0.5, 0]).add_tip()
        in_fn = MathTex("x(t)").next_to(in_arrow, LEFT)
        out_fn = MathTex("y(t)").next_to(out_arrow, RIGHT)
        system = VGroup(rec, rec_label)
        self.play(Create(system))
        self.play(Write(in_fn), Create(in_arrow))
        self.play(Write(out_fn), Create(out_arrow))
        self.wait(2)
        LCCDE = (
            MathTex(
                r"""a_n\frac{d^{n} y(t)}{dt^{n}}+
                        \cdots +a_{1}\frac{d y(t)}{dt}+a_{0}y(t)=b_m
                        \frac{d^{m} x(t)}{dt^{m}}+\cdots 
                        +b_{1}\frac{d x(t)}{dt}+b_{0}x(t)"""
            )
            .shift(DOWN * 2.5)
            .scale(0.8)
        )
        self.play(Write(LCCDE))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(LCCDE.animate.to_edge(UP, buff=0.7), FadeOut(VGroup(eq13, eq14)))
        laplace = (
            MathTex(
                r"""\mathcal{L}\left\{ f \right\}(s)=F(s)=\int_{0}^
                          {\infty}f(t)e^{-st}dt\qquad \mathcal{L}\left\{ \frac{d^n f}{dt^n} 
                          \right\}=s^nF(s)-\sum_{k=1}^{n}s^{n-k}f^{(k-1)}(0^-)"""
            )
            .scale(0.8)
            .to_edge(UP, buff=2)
        )
        self.play(Write(laplace))
        self.wait(2)
        laplace1 = (
            MathTex(
                r"""\mathcal{L}\left\{ f \right\}(s)=F(s)=\int_{0}^
                          {\infty}f(t)e^{-st}dt\qquad \mathcal{L}\left\{ \frac{d^n f}{dt^n} 
                          \right\}=s^nF(s)"""
            )
            .scale(0.8)
            .to_edge(UP, buff=2)
        )
        self.play(TransformMatchingShapes(laplace, laplace1))
        self.wait(2)
        LCCDE1 = (
            MathTex(
                r"""a_ns^nY(s)+\cdots +a_{1}sY(s)+a_{0}Y(s)=b_ms^mX(s)+\cdots +b_{1}sX(s)+b_{0}X(s)"""
            )
            .scale(0.8)
            .to_edge(DOWN, buff=1.1)
        )
        self.play(TransformFromCopy(LCCDE, LCCDE1))
        self.wait(1)
        LCCDE2 = (
            MathTex(
                r"""\left(a_ns^n+\cdots +a_{1}s+a_{0}\right)Y(s)=\left(b_ms^m+\cdots+b_{1}s+b_{0}\right)X(s)"""
            )
            .scale(0.8)
            .to_edge(DOWN, buff=1.1)
        )
        self.play(TransformMatchingShapes(LCCDE1, LCCDE2))
        self.wait(1)
        LCCDE3 = (
            MathTex(
                r"""Y(s)=\frac{\left(b_ms^m+\cdots+b_{1}s+b_{0}\right)}{\left(a_ns^n+\cdots +a_{1}s+a_{0}\right)}X(s)"""
            )
            .scale(0.8)
            .to_edge(DOWN, buff=0.8)
        )
        self.play(TransformMatchingShapes(LCCDE2, LCCDE3))
        self.wait(1)
        LCCDE4 = MathTex(r"""Y(s)=H(s)X(s)""").scale(0.8).to_edge(DOWN, buff=1.1)
        self.play(TransformMatchingShapes(LCCDE3, LCCDE4))
        self.wait(1)
        LCCDE5 = (
            MathTex(
                r"""\mathcal{L}^{-1}\left\{Y(s)\right\}=\mathcal{L}^{-1}\left\{H(s)X(s)\right\}"""
            )
            .scale(0.8)
            .to_edge(DOWN, buff=1.1)
        )
        self.play(TransformMatchingShapes(LCCDE4, LCCDE5))
        self.wait(1)
        LCCDE6 = MathTex(r"""y(t)=h(t)\ast x(t)""").scale(0.8).to_edge(DOWN, buff=1.1)
        self.play(TransformMatchingShapes(LCCDE5, LCCDE6))
        self.wait(1)
        LCCDE7 = (
            MathTex(r"""y(t)=h(t)\ast \delta(t)=h(t)""")
            .scale(0.8)
            .to_edge(DOWN, buff=1.1)
        )
        self.play(TransformMatchingShapes(LCCDE6, LCCDE7))
        self.wait(1)
        in_fn1 = MathTex(r"""\delta(t)""").next_to(in_arrow, LEFT)
        out_fn1 = MathTex("h(t)").next_to(out_arrow, RIGHT)
        self.play(Transform(in_fn, in_fn1), Transform(out_fn, out_fn1))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        HLCCDE = (
            MathTex(
                r"""a_n\frac{d^{n} y(t)}{dt^{n}}+
                        \cdots +a_{1}\frac{d y(t)}{dt}+a_{0}y(t)=0"""
            )
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE1 = (
            MathTex(
                r"""a_n\frac{d^{n} e^{\lambda t}}{dt^{n}}+\cdots +a_{1}\frac{d e^{\lambda t}}{dt}+a_{0}e^{\lambda t}=0"""
            )
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE2 = (
            MathTex(
                r"""\left(a_n\lambda^n+\cdots +a_{1}\lambda+a_{0}\right)e^{\lambda t}=0"""
            )
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE3 = (
            MathTex(r"""a_n\lambda^n+\cdots +a_{1}\lambda+a_{0}=0""")
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE4 = (
            MathTex(r"""(\lambda-p_1)(\lambda-p_2)\cdots (\lambda-p_n)=0""")
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE5 = (
            MathTex(r"""\lambda_1=p_1,\lambda_2=p_2,\cdots,\lambda_n=p_n""")
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        HLCCDE6 = (
            Tex(
                r"""$y(t)=c_1e^{p_1t}+c_2e^{p_2t}+\cdots+c_ne^{p_nt}$ for zero input $x(t)=0$"""
            )
            .to_edge(UP, buff=2)
            .scale(0.8)
        )
        constraints = (
            Tex(
                r"""solve for $c_1,c_2,...,c_n$ using $y(0^-)=k_1\quad\dot y(0^-)=k_2\quad\cdots\ \quad y^{(n-1)}(0^-)=k_n$"""
            )
            .to_edge(UP, buff=3.15)
            .scale(0.8)
        )
        self.play(
            FadeOut(
                VGroup(laplace1, LCCDE7, system, in_arrow, out_arrow, in_fn, out_fn)
            ),
            TransformFromCopy(LCCDE, HLCCDE),
        )
        self.wait(2)
        self.play(TransformMatchingShapes(HLCCDE, HLCCDE1))
        self.wait(1)
        self.play(TransformMatchingShapes(HLCCDE1, HLCCDE2))
        self.wait(1)
        self.play(TransformMatchingShapes(HLCCDE2, HLCCDE3))
        self.wait(1)
        self.play(TransformMatchingShapes(HLCCDE3, HLCCDE4))
        self.wait(1)
        self.play(TransformMatchingShapes(HLCCDE4, HLCCDE5))
        self.wait(1)
        self.play(TransformMatchingShapes(HLCCDE5, HLCCDE6))
        self.wait(2)
        self.play(Write(constraints))
        self.wait(2)

        poles = (
            Tex(
                r"""$p_1,p_2,...,p_n$ are $n$ distinct roots of the """,
                r"""characteristic equation $a_n\lambda^n+\cdots +
                a_{1}\lambda+a_{0}=0$""",
                " and are ",
                "poles",
                " of the ",
                r"""transfer function $$H(s)=\frac{\left(b_ms^m+
                \cdots+b_{1}s+b_{0}\right)}{\left(a_ns^n+\cdots +a_{1}s+a_{0}\right)}=\frac{(s-z_1)(s-z_2)
                \cdots (s-z_m)}{(s-p_1)(s-p_2)\cdots (s-p_n)}$$""",
            )
            .to_edge(UP, buff=4.3)
            .scale(0.8)
        )
        poles[1].set_color(YELLOW)
        poles[3].set_color(YELLOW)
        poles[5].set_color(YELLOW)
        self.play(Write(poles))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)
        SHM = (
            MathTex(
                r"""\ddot x+2\zeta\omega_n\dot x+\omega_n^2 x=\omega_n^2\frac{F_{\text{external}}}{k}"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        self.play(FadeOut(VGroup(LCCDE, HLCCDE6, constraints, poles)), Write(SHM))
        self.wait(2)
        lti_2nd_order = (
            MathTex(
                r"""\frac{d^2 c(t) }{dt^2}+2\zeta\omega_n\frac{d c(t) }{dt} +\omega_n^2 c(t)=\omega_n^2r(t)"""
            )
            .to_edge(UP, buff=1)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(SHM, lti_2nd_order))
        self.wait(2)
        second_order_tf = (
            MathTex(
                r"""\left(s^2+2\zeta\omega_ns +\omega_n^2\right) C(s)=\omega_n^2R(s)"""
            )
            .to_edge(UP, buff=3)
            .scale(1.5)
        )
        self.play(TransformFromCopy(lti_2nd_order, second_order_tf))
        self.wait(2)
        second_order_tf1 = (
            MathTex(
                r"""\frac{C(s)}{R(s)}=\frac{\omega_n^2}{s^2+2\zeta\omega_ns +\omega_n^2}"""
            )
            .to_edge(UP, buff=3)
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(second_order_tf, second_order_tf1))
        self.wait(2)
        second_order_ceq = (
            MathTex(r"""s^2+2\zeta\omega_ns +\omega_n^2=0""")
            .to_edge(UP, buff=5.2)
            .scale(1.5)
        )
        self.play(Write(second_order_ceq))
        self.wait(2)
        second_order_roots = (
            MathTex(r"""s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}""")
            .to_edge(UP, buff=6.65)
            .scale(1.5)
        )
        self.play(Write(second_order_roots))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Tracker variable
        omega_t = ValueTracker(5**0.5)
        zeta_t = ValueTracker(0.4472135955)
        omega = always_redraw(
            lambda: MathTex(r"""\omega_n=""", f"{omega_t.get_value():.2f}")
            .scale(0.9)
            .to_edge(LEFT, buff=0.45)
            .to_edge(UP, buff=2.2)
            .set_color(YELLOW)
            .set_z_index(1)
        )
        zeta = always_redraw(
            lambda: MathTex(r"""\zeta=""", f"{zeta_t.get_value():.2f}")
            .scale(0.9)
            .to_edge(LEFT, buff=0.45)
            .to_edge(UP, buff=3)
            .set_color(YELLOW)
            .set_z_index(1)
        )

        grid = NumberPlane().set_z_index(-1)
        self.play(
            FadeOut(VGroup(lti_2nd_order, second_order_tf1, second_order_ceq)),
            Create(grid),
            second_order_roots.animate.scale(0.6)
            .to_edge(LEFT, buff=0.45)
            .to_edge(UP, buff=1.2)
            .set_color(YELLOW)
            .set_z_index(1),
        )
        self.play(Write(omega), Write(zeta))

        x_mark1 = always_redraw(
            lambda: Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(
                [
                    -1 * zeta_t.get_value() * omega_t.get_value(),
                    -1 * omega_t.get_value() * (1 - zeta_t.get_value() ** 2) ** 0.5,
                    1,
                ]
            )
        )
        x_mark2 = always_redraw(
            lambda: Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(
                [
                    -1 * zeta_t.get_value() * omega_t.get_value(),
                    omega_t.get_value() * (1 - zeta_t.get_value() ** 2) ** 0.5,
                    1,
                ]
            )
        )

        const_wn = always_redraw(
            lambda: DashedVMobject(
                ParametricFunction(
                    lambda t: [
                        omega_t.get_value() * math.cos(t),
                        omega_t.get_value() * math.sin(t),
                        1,
                    ],
                    t_range=[0, 2 * PI],
                ),
                num_dashes=50,
            )
        )
        const_zeta1 = always_redraw(
            lambda: DashedVMobject(
                ParametricFunction(
                    lambda t: [
                        (-1 * zeta_t.get_value() * omega_t.get_value()) * t,
                        (
                            -1
                            * omega_t.get_value()
                            * (1 - zeta_t.get_value() ** 2) ** 0.5
                        )
                        * t,
                        1,
                    ],
                    t_range=[0, 10],
                ),
                num_dashes=50,
            )
        )
        const_zeta2 = always_redraw(
            lambda: DashedVMobject(
                ParametricFunction(
                    lambda t: [
                        (-1 * zeta_t.get_value() * omega_t.get_value()) * t,
                        (omega_t.get_value() * (1 - zeta_t.get_value() ** 2) ** 0.5)
                        * t,
                        1,
                    ],
                    t_range=[0, 10],
                ),
                num_dashes=50,
            )
        )
        self.play(Create(VGroup(const_wn, const_zeta1, const_zeta2)))
        self.play(Create(VGroup(x_mark1, x_mark2)))
        self.play(omega_t.animate.set_value(2**0.5))
        self.play(zeta_t.animate.set_value(-(0.5**0.5)))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        second_order_roots2 = (
            MathTex(r"""s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=0.2\pm 2j""")
            .scale(0.9)
            .to_edge(LEFT, buff=0.45)
            .to_edge(UP, buff=1.2)
            .set_z_index(1)
        )
        axes1 = (
            Axes(
                x_length=13,
                y_length=4.5,
                tips=False,
                axis_config={"include_ticks": False},
                x_range=[0, 13],
                y_range=[-8, 8],
            )
            .to_edge(LEFT, buff=0.45)
            .to_edge(DOWN, buff=1.2)
        )
        self.play(
            FadeOut(
                VGroup(
                    grid,
                    const_wn,
                    const_zeta1,
                    const_zeta2,
                    x_mark1,
                    x_mark2,
                    omega,
                    zeta,
                )
            ),
            TransformMatchingShapes(second_order_roots, second_order_roots2),
        )
        self.play(Create(axes1))
        response1 = (
            MathTex(r""" y(t)=-0.5e^{0.2t}\sin (2t)""")
            .scale(0.9)
            .to_edge(RIGHT, buff=1)
            .to_edge(UP, buff=1.2)
            .set_z_index(1)
        )
        self.play(Write(response1))
        graph_response1 = axes1.plot(
            lambda x: -0.5 * math.exp(0.2 * x) * math.sin(2 * x), x_range=[0, 13]
        ).set_color(YELLOW)
        self.play(Create(graph_response1))
        self.wait(2)
        response2 = (
            MathTex(r""" y(t)=-0.5e^{-0.2t}\sin (2t)""")
            .scale(0.9)
            .to_edge(RIGHT, buff=1)
            .to_edge(UP, buff=1.2)
            .set_z_index(1)
        )
        second_order_roots3 = (
            MathTex(r"""s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=-0.2\pm 2j""")
            .scale(0.9)
            .to_edge(LEFT, buff=0.45)
            .to_edge(UP, buff=1.2)
            .set_z_index(1)
        )
        self.play(
            TransformMatchingShapes(response1, response2),
            TransformMatchingShapes(second_order_roots2, second_order_roots3),
        )
        graph_response2 = axes1.plot(
            lambda x: -0.5 * math.exp(-0.2 * x) * math.sin(2 * x), x_range=[0, 13]
        ).set_color(YELLOW)
        self.play(Transform(graph_response1, graph_response2))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        eq15 = (
            MathTex(
                r"""s^2+2\zeta\omega_ns +\omega_n^2=0 \quad \Longrightarrow \quad s=p_1\quad\text{or}\quad s=p_2 """
            ).to_edge(UP, buff=1)
        ).set_color_by_gradient(YELLOW, WHITE)
        eq16 = (
            BulletedList(
                r"""$p_1 \neq  p_2 \quad \text{and} \quad p_1,p_2\in \mathbb{R} \quad 
                \Longrightarrow \quad y(t)=c_1e^{p_1 t}+c_2e^{p_2 t}$""",
                r"""$p_1 =  p_2 \quad \text{and} \quad p_1,p_2\in \mathbb{R} \quad 
                \Longrightarrow \quad y(t)=c_1e^{p_1 t}+c_2te^{p_1 t}$""",
                r"""$p_1 =\sigma+j\omega\quad \text{and} \quad p_2=\sigma-j\omega \quad
                \Longrightarrow \quad y(t)=e^{\sigma t}\left[c_1\cos(\omega t)+c_2\sin(\omega t)\right]$""",
            )
            .scale(0.8)
            .to_edge(UP, buff=2)
            .to_edge(LEFT, buff=0.7)
        )
        self.play(
            FadeOut(
                VGroup(
                    axes1,
                    graph_response1,
                    graph_response2,
                    response2,
                    second_order_roots3,
                )
            ),
            Write(eq15),
        )
        self.play(Write(eq16))
        self.wait(2)
        text = (
            Tex(
                r"""For an LTI system to be stable, the zero-input response \\ 
                   of the system, due to initial conditions, has to decay \\ 
                   as $t\to \infty$, this allows the output $y(t)$ to eventually  \\ 
                   approach the input $x(t)$ even when it is not zero."""
            )
            .to_edge(UP, buff=4.8)
            .set_color_by_gradient(YELLOW, WHITE)
        )
        self.play(Write(text))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        RE = ValueTracker(-5)
        IM = ValueTracker(0)

        self.play(FadeOut(VGroup(eq15, eq16, text)), Create(grid))
        self.wait(2)

        # One root on the real axis
        x_mark = always_redraw(
            lambda: Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(
                [
                    RE.get_value(),
                    0,
                    1,
                ]
            )
        )
        self.play(Create(x_mark))
        Frame = always_redraw(
            lambda: RoundedRectangle(
                corner_radius=0.1,
                width=3,
                height=2,
                stroke_color=color_gradient([YELLOW, WHITE], 7),
                stroke_width=10,
                fill_opacity=0.7,
                color=BLACK,
            ).move_to([RE.get_value(), 2, 9])
        )

        def A():
            return 0 if RE.get_value() <= 0 else -5

        def B():
            return 5 if RE.get_value() <= 0 else 0

        Axis = always_redraw(
            lambda: Axes(
                x_length=2,
                y_length=2,
                tips=False,
                axis_config={"include_ticks": False, "stroke_opacity": 0},
                x_range=[A(), B()],
                y_range=[-1.5, 1.5],
            ).move_to([RE.get_value(), 2, 10])
        )
        Curve = always_redraw(
            lambda: Axis.plot(
                lambda x: math.exp(RE.get_value() * x), x_range=[A(), B()]
            ).set_color(YELLOW)
        )
        self.play(Create(VGroup(Axis, Frame, Curve)))
        self.wait(2)
        self.play(RE.animate.set_value(0), run_time=3)
        self.wait(2)
        self.play(RE.animate.set_value(5), run_time=3)
        self.wait(2)

        # Complex conjugate roots
        x_mark1 = always_redraw(
            lambda: Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(
                [
                    RE.get_value(),
                    IM.get_value(),
                    0,
                ]
            )
        )
        x_mark2 = always_redraw(
            lambda: Cross(scale_factor=0.2, stroke_color=YELLOW).move_to(
                [
                    RE.get_value(),
                    -1 * IM.get_value(),
                    0,
                ]
            )
        )
        Frame1 = always_redraw(
            lambda: RoundedRectangle(
                corner_radius=0.1,
                width=3,
                height=2,
                stroke_color=color_gradient([YELLOW, WHITE], 7),
                stroke_width=10,
                fill_opacity=0.7,
                color=BLACK,
            ).move_to([RE.get_value(), 0, 9])
        )

        def A():
            return 0 if RE.get_value() <= 0 else -5

        def B():
            return 5 if RE.get_value() <= 0 else 0

        Axis1 = always_redraw(
            lambda: Axes(
                x_length=2,
                y_length=2,
                tips=False,
                axis_config={"include_ticks": False, "stroke_opacity": 0},
                x_range=[A(), B()],
                y_range=[-1.5, 1.5],
            ).move_to([RE.get_value(), 0, 10])
        )
        Curve1 = always_redraw(
            lambda: Axis1.plot(
                lambda x: math.exp(RE.get_value() * x)
                * math.cos((10 / 3) * IM.get_value() * x),
                x_range=[A(), B()],
            ).set_color(YELLOW)
        )
        self.remove(x_mark)
        self.add(x_mark1, x_mark2)
        self.play(Frame.animate.shift(DOWN * 2), Axis.animate.shift(DOWN * 2))
        self.remove(Frame, Axis, Curve)
        self.add(Frame1, Axis1, Curve1)
        self.wait(2)
        self.play(IM.animate.set_value(3), run_time=3)
        self.wait(2)
        self.play(RE.animate.set_value(0), run_time=3)
        self.wait(2)
        self.play(RE.animate.set_value(-5), run_time=3)
        self.wait(2)
        self.play(FadeOut(VGroup(x_mark1, x_mark2, Frame1, Axis1, Curve1)))

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        stable = Rectangle(
            stroke_width=0,
            color=YELLOW,
            fill_opacity=0.3,
            width=config.frame_width / 2,
            height=config.frame_height,
        ).move_to([-1 * config.frame_width / 4, 0, 0])
        stable_label = (
            Tex("Stable Region")
            .scale(1.5)
            .move_to(stable)
            .shift(UP * 2)
            .set_z_index(10)
        )
        margin = Line(
            start=[0, -1 * config.frame_height / 2, 10],
            end=[0, config.frame_height / 2, 0],
            color=YELLOW,
            stroke_width=10,
        )
        margin_label = (
            Tex("Marginally Stable Region")
            .scale(1.2)
            .next_to(margin)
            .shift(UP * 2)
            .set_z_index(10)
        )
        unstable = Rectangle(
            stroke_width=0,
            color=YELLOW,
            fill_opacity=0.3,
            width=config.frame_width / 2,
            height=config.frame_height,
        ).move_to([config.frame_width / 4, 0, 0])
        unstable_label = (
            Tex("Unstable Region")
            .scale(1.5)
            .move_to(unstable)
            .shift(UP * 2)
            .set_z_index(10)
        )
        self.play(FadeIn(VGroup(stable, stable_label)))
        self.wait(2)
        self.play(
            FadeOut(VGroup(stable, stable_label)), FadeIn(VGroup(margin, margin_label))
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(margin, margin_label)),
            FadeIn(VGroup(unstable, unstable_label)),
        )
        self.wait(2)
        self.play(FadeOut(VGroup(unstable, unstable_label)))

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(FadeOut(grid))
        rec1 = Rectangle(height=1, width=2, color=YELLOW).shift(UP * 1.5)
        rec1_label = Tex("$G(s)$").move_to(rec1)
        rec2 = Rectangle(height=1, width=2, color=YELLOW).shift(DOWN * 1.5)
        rec2_label = Tex("$H(s)$").move_to(rec2)
        in_arrow1 = Line(start=[-4, 1.5, 0], end=[-2.95, 1.5, 0]).add_tip()
        plus = (
            MathTex("+").scale(0.8).next_to(in_arrow1, UP).shift((0.525 - 0.1) * RIGHT)
        )
        in_arrow2 = Line(start=[-2.05, 1.5, 0], end=[-1, 1.5, 0]).add_tip()
        out_arrow = Line(start=[1, 1.5, 0], end=[4, 1.5, 0]).add_tip()
        feed_arrow1 = VGroup(
            Line(start=[2.5, 1.5, 0], end=[2.5, -1.5, 0]),
            Line(start=[2.5, -1.5, 0], end=[1, -1.5, 0]).add_tip(),
        )
        feed_arrow2 = VGroup(
            Line(start=[-1, -1.5, 0], end=[-2.5, -1.5, 0]),
            Line(start=[-2.5, -1.5, 0], end=[-2.5, 1.05, 0]).add_tip(),
        )
        minus = (
            MathTex("-").scale(0.8).next_to(feed_arrow2, LEFT).shift((1.275 - 0.2) * UP)
        )
        in_fn = MathTex("X(s)").next_to(in_arrow1, LEFT)
        out_fn = MathTex("Y(s)").next_to(out_arrow, RIGHT)
        G = VGroup(rec1, rec1_label)
        H = VGroup(rec2, rec2_label)
        summing_point = VGroup(
            Circle(radius=0.45, color=WHITE).move_to([-2.5, 1.5, 0]),
            Cross(
                stroke_width=DEFAULT_STROKE_WIDTH,
                scale_factor=0.318198,
                stroke_color=WHITE,
            ).move_to([-2.5, 1.5, 0]),
        )
        self.play(Write(in_fn), Create(in_arrow1), Write(plus))
        self.play(Create(summing_point))
        self.play(Create(in_arrow2))
        self.play(Create(G))
        self.play(Write(out_fn), Create(out_arrow))
        self.play(Create(feed_arrow1))
        self.play(Create(H))
        self.play(Create(feed_arrow2), Write(minus))
        self.wait(2)
        block_diagram = VGroup(
            in_fn,
            in_arrow1,
            plus,
            in_arrow2,
            summing_point,
            G,
            out_fn,
            out_arrow,
            feed_arrow1,
            feed_arrow2,
            H,
            minus,
        )
        self.play(
            block_diagram.animate.scale(0.6)
            .to_edge(UP, buff=1)
            .to_edge(RIGHT, buff=0.3)
        )
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        tf1 = (
            MathTex("Y(s)=G(s)[X(s)-H(s)Y(s)]")
            .to_edge(UP, buff=1)
            .to_edge(LEFT, buff=0.3)
        )
        self.play(Write(tf1))
        tf2 = (
            MathTex("Y(s)=G(s)X(s)-G(s)H(s)Y(s)]")
            .to_edge(UP, buff=2.5)
            .to_edge(LEFT, buff=0.3)
        )
        self.play(TransformFromCopy(tf1, tf2))
        self.wait(2)
        tf3 = (
            MathTex("Y(s)+G(s)H(s)Y(s)=G(s)X(s)")
            .to_edge(UP, buff=2.5)
            .to_edge(LEFT, buff=0.3)
        )
        self.play(TransformMatchingShapes(tf2, tf3))
        self.wait(2)
        tf4 = (
            MathTex("Y(s)[1+G(s)H(s)]=G(s)X(s)")
            .to_edge(UP, buff=2.5)
            .to_edge(LEFT, buff=0.3)
        )
        self.play(TransformMatchingShapes(tf3, tf4))
        self.wait(2)
        tf5 = (
            MathTex(r"""T(s)=\frac{Y(s)}{X(s)}=\frac{G(s)}{1+G(s)H(s)}""")
            .set_color_by_gradient(YELLOW, WHITE)
            .to_edge(UP, buff=2.2)
            .to_edge(LEFT, buff=0.3)
        )
        self.play(TransformMatchingShapes(tf4, tf5))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        ceq1 = MathTex(r"""1+G(s)H(s)=0""").to_edge(UP, buff=4.3)
        self.play(Write(ceq1))
        self.wait(2)
        ceq2 = MathTex(r"""G(s)H(s)=-1""").to_edge(UP, buff=4.3)
        self.play(TransformMatchingShapes(ceq1, ceq2))
        self.wait(2)
        ceq3 = MathTex(
            r"""K\frac{(s-z_1)(s-z_2)\cdots (s-z_m)}{(s-p_1)(s-p_2)\cdots (s-p_n)}=-1"""
        ).to_edge(UP, buff=4.1)
        self.play(TransformMatchingShapes(ceq2, ceq3))
        self.wait(2)
        ceq4 = MathTex(
            r"""K(s-z_1)(s-z_2)\cdots (s-z_m)+(s-p_1)(s-p_2)\cdots (s-p_n)=0"""
        ).to_edge(UP, buff=4.3)
        self.play(TransformMatchingShapes(ceq3, ceq4))
        self.wait(2)
        roots = MathTex(
            r"""K=0\Rightarrow  s\in \{ p_1,p_2,\cdots,p_n\} \ \ \quad K\to \infty \Rightarrow  s
            \in \{ z_1,z_2,\cdots,z_m\} \\\text{if} \quad q=n-m>0\quad\text{ then} \qquad K\to \infty 
            \quad \text{also when} \quad s\to \infty""",
            color=YELLOW,
        ).to_edge(UP, buff=5.8)
        self.play(Write(roots))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(FadeOut(roots), TransformMatchingShapes(ceq4, ceq2))
        magnitude = MathTex(
            r"""\left| G(s)H(s) \right|=K\frac{|s-z_1||s-z_2|\cdots |s-z_m|}{|s-p_1||s-p_2|\cdots |s-p_n|}=1""",
            color=YELLOW,
        ).to_edge(UP, buff=4.3)
        angle = MathTex(
            r"""\angle \left( G(s)H(s) \right)=\sum_{i=1}^{m}\angle (s-z_i)-\sum_{i=1}^{n}\angle (s-p_i)=\pi""",
            color=YELLOW,
        ).to_edge(UP, buff=5.8)
        self.wait(2)
        self.play(TransformMatchingShapes(ceq2, VGroup(magnitude, angle)))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(
            FadeOut(VGroup(block_diagram, angle, magnitude, tf5, tf1)), Create(grid)
        )
        self.wait(2)
        system = (
            MathTex("1+", "K", r"\frac{s^3+7s^2+24s+18}{s^4+9s^3+29s^2+55s+50}")
            .scale(0.7)
            .to_corner(UR, buff=1.1)
        )
        system[1].set_color(YELLOW)
        self.play(Write(system))
        self.wait(2)

        D = [1, 9, 29, 55, 50]
        poles = [[z.real, z.imag, 1] for z in np.roots(D)]

        N = [0, 1, 7, 24, 18]
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

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        K = ValueTracker(0)

        def ceqf(k):
            ceq = []
            for i in range(len(D)):
                p = D[i]
                z = N[i]
                ceq.append(p + z * k)
            return ceq

        root_locus1 = always_redraw(
            lambda: ParametricFunction(
                lambda t: [
                    np.roots(ceqf(t))[0].real,
                    np.roots(ceqf(t))[0].imag,
                    1,
                ],
                t_range=[0, K.get_value()],
                color=YELLOW,
                stroke_width=6,
            )
        )
        root_locus2 = always_redraw(
            lambda: ParametricFunction(
                lambda t: [
                    np.roots(ceqf(t))[1].real,
                    np.roots(ceqf(t))[1].imag,
                    1,
                ],
                t_range=[0, K.get_value()],
                color=YELLOW,
                stroke_width=6,
            )
        )
        root_locus3 = always_redraw(
            lambda: ParametricFunction(
                lambda t: [
                    np.roots(ceqf(t))[2].real,
                    np.roots(ceqf(t))[2].imag,
                    1,
                ],
                t_range=[0, K.get_value()],
                color=YELLOW,
                stroke_width=6,
            )
        )
        root_locus4 = always_redraw(
            lambda: ParametricFunction(
                lambda t: [
                    np.roots(ceqf(t))[3].real,
                    np.roots(ceqf(t))[3].imag,
                    1,
                ],
                t_range=[0, K.get_value()],
                color=YELLOW,
                stroke_width=6,
            )
        )
        self.add(root_locus1, root_locus2, root_locus3, root_locus4)
        self.play(K.animate.set_value(60))
        self.wait(5)

class fin(VectorScene):
    def construct(self):

        eq81 = (
            Tex(
                r"""Fin.""",
            )
            .scale(6)
            .set_color_by_gradient(YELLOW, WHITE)
        )
        self.play(Write(eq81), run_time=6)
        self.wait(2)
