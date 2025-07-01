from manim import *
from manim_physics import *
from scipy.integrate import quad
import math

#config.background_color = "#00001a"
Last = 1


class Fourier(VectorScene):
    def construct(self):
        # Define and play vectors u, v, and the plane
        self.next_section(skip_animations=Last)
        plane = NumberPlane()
        u = Vector([-3, -1, 0], color=ORANGE, z_index=3, tip_shape=StealthTip)
        labelu = self.get_vector_label(
            u, Tex(r"$$\textbf{u}$$", color=ORANGE), direction=UP
        )
        v = Vector([-2, 2, 0], color=RED, z_index=1, tip_shape=StealthTip)
        labelv = self.get_vector_label(
            v, Tex(r"$$\textbf{v}$$", color=RED), direction=DOWN
        )
        self.add(plane)
        for V in [(u, labelu), (v, labelv)]:
            self.add_vector(V[0])
            self.play(FadeIn(V[1]))

        # Create the projection of u onto v
        projv = v.get_projection(
            u.get_end()
        )  # Get the coordinates of the projection point
        proj_linev = DashedLine(
            u.get_end(), projv, color=YELLOW
        )  # Create a dashed line from v1 to the projection point
        dot1v = Dot(
            projv, color=YELLOW, z_index=4, radius=0.05
        )  # Create a dot at the projection point
        dot2v = Dot(u.get_end(), color=YELLOW, z_index=4, radius=0.05)
        pv = Vector(projv, color=YELLOW, z_index=3, tip_shape=StealthTip)
        pv.tip.z_index = 3
        ra1 = RightAngle(proj_linev, pv, quadrant=(-1, 1), length=0.25, color=YELLOW)

        # Add the vector and the projection to the scene
        self.play(FadeIn(dot2v), FadeIn(dot1v))
        self.play(Create(proj_linev))
        self.play(Create(ra1))
        self.play(TransformFromCopy(u, pv))
        eq1 = MathTex(
            r"""\text{proj}_\textbf{v}\textbf{u}=\frac{\textbf{u}\cdot
            \textbf{v}}{\textbf{v}\cdot \textbf{v}}\textbf{v}""",
            color=YELLOW,
        ).to_edge(UP, buff=1.1)
        self.play(Write(eq1))

        # Normalize vector v
        self.play(FadeOut(VGroup(dot1v, dot2v, proj_linev, pv, ra1)))
        eq2 = MathTex(
            r"""\mathbf{\hat{v}}=\frac{\mathbf{v}}{\mathbf{\left\| v\right\|}}""",
            color=RED,
        ).to_edge(LEFT, buff=0.8)
        eq2.to_edge(UP, buff=0.8 * 3)
        self.play(Write(eq2))
        vn = Vector(
            [(1 / v.get_length()) * c for c in v.get_end()],
            color=RED,
            z_index=3,
            tip_shape=StealthTip,
        )
        labelvn = self.get_vector_label(
            vn, MathTex(r"\mathbf{\hat{v}}", color=RED), direction=DOWN
        )
        self.play(Transform(v, vn), FadeOut(labelv), FadeIn(labelvn))
        self.remove(v)
        self.add(vn)

        # Create the projection of u onto vn
        projv = vn.get_projection(
            u.get_end()
        )  # Get the coordinates of the projection point
        proj_linev = DashedLine(
            u.get_end(), projv, color=YELLOW
        )  # Create a dashed line from v1 to the projection point
        dot1v = Dot(
            projv, color=YELLOW, z_index=4, radius=0.05
        )  # Create a dot at the projection point
        dot2v = Dot(u.get_end(), color=YELLOW, z_index=4, radius=0.05)
        pv = Vector(projv, color=YELLOW, z_index=3, tip_shape=StealthTip)
        pv.tip.z_index = 3
        ra1 = RightAngle(proj_linev, pv, quadrant=(-1, -1), length=0.25, color=YELLOW)

        # Add the vector and the projection to the scene
        self.play(FadeIn(dot2v), FadeIn(dot1v))
        self.play(Create(proj_linev))
        self.play(Create(ra1))
        self.play(TransformFromCopy(u, pv))
        eq3 = MathTex(
            r"""\text{proj}_\textbf{v}\textbf{u}=\frac{\textbf{u}\cdot
            \textbf{v}}{\textbf{v}\cdot \textbf{v}}\textbf{v}=\text{proj}_\mathbf{\hat{v}}
            \mathbf{u}=(\mathbf{u}\cdot \mathbf{\hat{v}})\mathbf{\hat{v}}""",
            color=YELLOW,
        ).to_edge(UP, buff=1.1)
        self.play(Transform(eq1, eq3))
        self.wait(3)

        ####################################################################################################################

        # Define vector wn and add it to scene
        self.next_section(skip_animations=Last)
        self.remove(eq1)
        self.play(FadeOut(VGroup(dot1v, dot2v, proj_linev, pv, eq2, eq3, ra1)))
        wn = Vector(
            [2**0.5 / 2, 2**0.5 / 2], color=GREEN, z_index=3, tip_shape=StealthTip
        )
        labelwn = self.get_vector_label(
            wn, MathTex(r"\mathbf{\hat{w}}", color=GREEN), direction=UP
        )
        self.add_vector(wn)
        self.play(FadeIn(labelwn))
        ra3 = RightAngle(vn, wn, length=0.25, color=YELLOW)
        self.play(Create(ra3))

        # Create the projection of u onto wn
        projw = wn.get_projection(
            u.get_end()
        )  # Get the coordinates of the projection point
        proj_linew = DashedLine(
            u.get_end(), projw, color=YELLOW
        )  # Create a dashed line from v1 to the projection point
        dot1w = Dot(
            projw, color=YELLOW, z_index=4, radius=0.05
        )  # Create a dot at the projection point
        dot2w = Dot(u.get_end(), color=YELLOW, z_index=4, radius=0.05)
        pw = Vector(projw, color=YELLOW, z_index=3, tip_shape=StealthTip)
        pv.tip.z_index = 3
        ra2 = RightAngle(proj_linew, pw, quadrant=(-1, -1), length=0.25, color=YELLOW)

        # Add the vector and the projection to the scene
        self.play(FadeIn(dot2w), FadeIn(dot1w))
        self.play(Create(proj_linew))
        self.play(Create(ra2))
        self.play(TransformFromCopy(u, pw))
        eq4 = MathTex(
            r"""\text{proj}_\mathbf{\hat{w}}\mathbf{u}=(\mathbf{u}\cdot \mathbf{\hat{w}})\mathbf{\hat{w}}""",
            color=YELLOW,
        ).to_edge(UP, buff=1.1)
        self.play(Write(eq4))
        self.play(FadeIn(dot2v), FadeIn(dot1v))
        self.play(Create(proj_linev))
        self.play(Create(ra1))
        self.play(TransformFromCopy(u, pv))
        eq5 = MathTex(
            r"""\mathbf{u}=\text{proj}_\mathbf{\hat{v}}\mathbf{u}+\text{proj}_\mathbf
            {\hat{w}}\mathbf{u}=(\mathbf{u}\cdot \mathbf{\hat{v}})
            \mathbf{\hat{v}}+(\mathbf{u}\cdot \mathbf{\hat{w}})\mathbf{\hat{w}}""",
            color=YELLOW,
        ).to_edge(UP, buff=1.1)
        self.play(Transform(eq4, eq5))

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(
            FadeOut(
                VGroup(
                    ra1, ra2, dot1v, dot2v, dot1w, dot2w, proj_linev, pv, proj_linew, pw
                )
            )
        )
        eq6 = MathTex(
            r"""\mathbf{u}=(\mathbf{u}\cdot \mathbf{\hat{v}})
            \mathbf{\hat{v}}+(\mathbf{u}\cdot \mathbf{\hat{w}})\mathbf{\hat{w}}""",
            color=YELLOW,
        ).to_edge(UP, buff=1.1)
        self.play(
            FadeOut(VGroup(labelvn, labelwn)),
            Rotate(VGroup(vn, wn, ra3), -PI / 4, about_point=ORIGIN),
            Transform(eq4, eq6),
        )
        self.wait()
        projw = wn.get_projection(u.get_end())
        projv = vn.get_projection(u.get_end())
        pw = Vector(projw, color=YELLOW, z_index=3, tip_shape=StealthTip)
        pv = Vector(projv, color=YELLOW, z_index=3, tip_shape=StealthTip)
        self.play(TransformFromCopy(u, pv), TransformFromCopy(u, pw))
        self.play(
            FadeOut(VGroup(u, pv, pw, plane, labelu, wn, vn, ra3)),
            eq4.animate.set_color(TEAL),
        )
        self.wait()

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq7 = MathTex(
            r"""\mathbf{\hat{v}}\bot \mathbf{\hat{w}}\Longleftrightarrow \mathbf{\hat{v}}\cdot\mathbf{\hat{w}}=0""",
            color=WHITE,
        ).to_edge(UP, buff=2)
        self.play(Write(eq7))
        eq8 = MathTex(
            r"""\left\| \mathbf{\hat{v}} \right\|=\sqrt{\mathbf{\hat{v}}\cdot\mathbf{\hat{v}}}=1
            \quad\left\| \mathbf{\hat{w}} \right\|=\sqrt{\mathbf{\hat{w}}\cdot\mathbf{\hat{w}}}=1""",
            color=WHITE,
        ).to_edge(UP, buff=2.9)
        self.play(Write(eq8))
        eq9 = MathTex(
            r"""\text{span}\left\{ \mathbf{\hat{v}},\mathbf{\hat{w}} \right\}=\mathbb{R}^2""",
            color=WHITE,
        ).to_edge(UP, buff=2.9 + 0.9)
        self.play(Write(eq9))
        eq10 = MathTex(
            r"""\forall \mathbf{u}\in \mathbb{R}^2,\quad\mathbf{u}=(\mathbf{u}\cdot 
            \mathbf{\hat{v}})\mathbf{\hat{v}}+(\mathbf{u}\cdot \mathbf{\hat{w}})\mathbf{\hat{w}}""",
            color=WHITE,
        ).to_edge(UP, buff=2.9 + 0.9 * 2)
        self.play(Write(eq10))
        eq11 = MathTex(
            r"""\text{The set }""",
            r"""B=\left\{ \mathbf{\hat{v}},\mathbf{\hat{w}} \right\}""",
            r"""\text{ is an }""",
            r"""{\textbf{Orthonormal Basis}}""",
            r"""\text{ for } \mathbb{R}^2""",
            color=WHITE,
        ).to_edge(UP, buff=2.9 + 0.9 * 3)
        eq11[1].set_color(TEAL)
        eq11[3].set_color(TEAL)
        self.play(Write(eq11))
        self.wait()

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq12 = MathTex(
            r"""\textbf{Orthonormal Basis}""",
            color=TEAL,
        ).to_edge(UP, buff=1.1)
        self.play(
            FadeOut(VGroup(eq4, eq7, eq8, eq9, eq10)),
            TransformMatchingShapes(eq11, eq12),
        )
        eq13 = MathTex(
            r"""\text{If } B \text{ is an orthonormal basis for a vector space } V""",
            color=WHITE,
        ).to_edge(UP, buff=1.1 + 0.9)
        self.play(Write(eq13))
        eq14 = MathTex(
            r"""  \forall \mathbf{v}\in V ,\quad
            \mathbf{v}=\sum_{\mathbf{b}\in B}^{}\left\langle \mathbf{v},\mathbf{b} \right\rangle \mathbf{b}""",
            color=TEAL,
        ).to_edge(UP, buff=1.1 + 0.9 * 2)
        self.play(Write(eq14))
        eq15 = MathTex(
            r"""\text{where }""",
            r"""\left\langle \mathbf{v},\mathbf{b} \right\rangle""",
            r"""\text{ is the }""",
            r"""\textbf{Inner Product}""",
            r"""\text{ of } \mathbf{v} \text{ and }\mathbf{b}""",
            color=WHITE,
        ).to_edge(UP, buff=1.1 + 0.9 * 3 + 0.5)
        eq15[1].set_color(TEAL)
        eq15[3].set_color(TEAL)
        self.play(Write(eq15))
        eq16 = MathTex(
            r"""\text{which is the generalization of the dot product on } \mathbb{R}^n""",
            color=WHITE,
        ).to_edge(UP, buff=1.1 + 0.9 * 4 + 0.5)
        eq17 = MathTex(
            r"""\text{to an arbitrary vector space } V""",
            color=WHITE,
        ).to_edge(UP, buff=1.1 + 0.9 * 5 + 0.5)
        self.play(Write(eq16))
        self.play(Write(eq17))
        self.wait()

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq18 = MathTex(
            r"""\textbf{Inner Product}""",
            color=TEAL,
        ).to_edge(UP, buff=1.1)
        self.play(
            FadeOut(VGroup(eq12, eq13, eq14, eq16, eq17)),
            TransformMatchingShapes(eq15, eq18),
        )
        eq19 = Tex(
            r"""\textbf{Definition:} A""",
            r"""\textbf{ Hermitian inner product }""",
            r"""on a complex vector space $V$ is a function that, to each pair of vectors $\mathbf{u}$ and $\mathbf{v}$ in $V$, associates a complex number $\left\langle \mathbf{u},\mathbf{v} \right\rangle$ and satisfies the following axioms, for all $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w} \in V$ and $c \in \mathbb{C}$:""",
        ).to_edge(UP, buff=2)
        eq19.scale(0.75)
        eq19[1].set_color(TEAL)
        eq20 = (
            BulletedList(
                r"""\textbf{1.} $\left\langle \mathbf{u},\mathbf{v} \right\rangle=\overline{\left\langle \mathbf{v},\mathbf{u} \right\rangle}$.""",
                r"""\textbf{2.} $\left\langle \mathbf{u}+\mathbf{v},\mathbf{w} \right\rangle=\left\langle \mathbf{u},\mathbf{w} \right\rangle+\left\langle \mathbf{v},\mathbf{w} \right\rangle$ and $\left\langle \mathbf{u},\mathbf{v}+\mathbf{w} \right\rangle=\left\langle \mathbf{u},\mathbf{v}\right\rangle+\left\langle \mathbf{u},\mathbf{w} \right\rangle$.""",
                r"""\textbf{3.} $\left\langle c\mathbf{u},\mathbf{v}\right\rangle=c\left\langle \mathbf{u},\mathbf{v}\right\rangle$ and $\left\langle \mathbf{u},c\mathbf{v}\right\rangle=\overline{c}\left\langle \mathbf{u},\mathbf{v}\right\rangle$.""",
                r"""\textbf{4.} $\left\langle \mathbf{u},\mathbf{u}\right\rangle$ is a nonnegative real number and $\left\langle \mathbf{u},\mathbf{u}\right\rangle=0$ if and only if $\mathbf{u}=0$.)""",
            )
            .scale(0.75)
            .to_edge(UP, buff=4)
            .set_color(TEAL_A)
        )
        self.play(Write(eq19))
        self.play(Write(eq20))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(
            FadeOut(VGroup(eq18, eq19, eq20)),
        )
        eq21 = (
            Title(
                r"""\textbf{$L^2$ inner product space}""",
                color=TEAL,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(Write(eq21))
        eq22 = (
            Tex(
                r"""The set of all square-integrable functions defined on an interval\\$\left[-\frac{T_0}{2},
            \frac{T_0}{2}\right]$ is an inner product vector space, denoted $L^2\left(\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\right)$"""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        self.play(Write(eq22))
        eq23 = (
            Tex(
                r"""\textbf{$$x:\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\to \mathbb{C}\: \text{ square integrable on } \left[-\frac{T_0}{2},\frac{T_0}{2}\right]\quad \Longleftrightarrow \quad\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}\left|  x(t)\right|^2dt< \infty$$}""",
                color=TEAL,
                stroke_width=0.3,
            )
            .to_edge(UP, buff=3.3)
            .scale(0.7)
        )
        self.play(DrawBorderThenFill(eq23))
        eq24 = (
            Tex(
                r"""We define the inner product on this space as
                $$\left\langle x,y \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\overline{y(t)}dt$$"""
            )
            .to_edge(UP, buff=5)
            .scale(0.9)
        )
        self.play(Write(eq24))

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq25 = MathTex(
            r"""\left\langle x,y \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}""",
            r"""x(t)\overline{y(t)}dt""",
        ).to_edge(UP, buff=2)
        self.play(FadeOut(VGroup(eq22, eq23)), TransformMatchingShapes(eq24, eq25))
        self.wait()
        eq26 = MathTex(
            r"""\left\langle x,x \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}""",
            r"""x(t)\overline{x(t)}dt""",
        ).to_edge(UP, buff=2)
        self.play(ReplacementTransform(eq25, eq26))
        self.wait()
        eq27 = MathTex(
            r"""\left\langle x,x \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}""",
            r"""\left| x(t) \right|^2dt""",
        ).to_edge(UP, buff=2)
        self.play(TransformMatchingShapes(eq26[1], eq27[1]))
        self.wait()
        eq28 = (
            Tex(
                r"""A""",
                r""" \textbf{norm} """,
                r"""is a generalization of the intuitive notion of "length"\\in the physical world.""",
                r""" The norm is defined as""",
            )
            .to_edge(UP, buff=3.7)
            .scale(0.95)
        )
        eq28[1].set_color(TEAL)
        self.play(Write(eq28[:3]))
        self.wait(0.5)
        self.play(Write(eq28[-1]))
        eq29 = MathTex(
            r"""\left\| x(t) \right\|=\sqrt{\left\langle x,x \right\rangle}"""
        ).to_edge(UP, buff=5)
        self.play(Write(eq29))
        eq30 = MathTex(
            r"""\forall x\in L^2\left(\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\right)\quad \left\langle x,x \right\rangle<\infty"""
        ).to_edge(UP, buff=6)
        self.play(Write(eq30))
        self.wait()

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(
            FadeOut(VGroup(eq26[:1], eq26[2:], eq27[1], eq28, eq30)),
            eq29.animate.to_edge(UP, buff=2.2),
        )
        self.wait()
        eq31 = MathTex(
            r"""\forall m,n\in \mathbb{Z}^+\quad\left\langle \cos m\omega_0t,\cos n\omega_0t \right\rangle=\left\{\begin{matrix}
            0&m\neq n \\ 1&m=n \end{matrix}\right.\quad \omega_0=\frac{2\pi}{T_0}"""
        ).to_edge(UP, buff=3.2)
        self.play(Write(eq31))
        self.wait()
        eq32 = MathTex(
            r"""\cos m\omega_0t\bot \cos n\omega_0t\Longleftrightarrow \left\langle \cos m\omega_0t,\cos n\omega_0t \right\rangle=0\quad m\neq n"""
        ).to_edge(UP, buff=5)
        self.play(Write(eq32))
        eq33 = MathTex(
            r"""\left\| \cos n\omega_0t \right\|=\sqrt{\left\langle \cos n\omega_0t,\cos n\omega_0t \right\rangle}=1"""
        ).to_edge(UP, buff=6.2)
        self.play(Write(eq33))
        self.wait(3)
        eq34 = MathTex(
            r"""\forall m,n\in \mathbb{Z}^+\quad""",
            r"""\left\langle \sin m\omega_0t,\sin n\omega_0t \right\rangle=""",
            r"""\left\{\begin{matrix}
            0&m\neq n \\ 1&m=n \end{matrix}\right.\quad""",
            r"""\omega_0=\frac{2\pi}{T_0}""",
        ).to_edge(UP, buff=3.2)
        eq35 = MathTex(
            r"""\sin m\omega_0t\bot \sin n\omega_0t\Longleftrightarrow \left\langle \sin m\omega_0t,\sin n\omega_0t \right\rangle=0\quad m\neq n"""
        ).to_edge(UP, buff=5)
        eq36 = MathTex(
            r"""\left\| \sin n\omega_0t \right\|=\sqrt{\left\langle \sin n\omega_0t,\sin n\omega_0t \right\rangle}=1"""
        ).to_edge(UP, buff=6.2)
        self.play(
            TransformMatchingShapes(eq31, eq34),
            TransformMatchingShapes(eq32, eq35),
            TransformMatchingShapes(eq33, eq36),
        )
        self.wait(3)
        eq37 = MathTex(
            r"""\forall m,n\in \mathbb{Z}^+\quad""",
            r"""\left\langle\cos m\omega_0t,\sin n\omega_0t \right\rangle=""",
            r"""0 \quad""",
            r"""\omega_0=\frac{2\pi}{T_0}""",
        ).to_edge(UP, buff=3.2)
        eq38 = MathTex(
            r"""\cos m\omega_0t\bot \sin n\omega_0t\Longleftrightarrow \left\langle \cos m\omega_0t,\sin n\omega_0t \right\rangle=0"""
        ).to_edge(UP, buff=5)
        self.play(
            TransformMatchingShapes(eq34[1], eq37[1]),
            TransformMatchingShapes(eq34[2], eq37[2]),
            TransformMatchingShapes(eq35, eq38),
        )
        self.wait(3)
        eq39 = MathTex(
            r"""\forall m,n\in \mathbb{Z}^+\quad""",
            r"""\left\langle1,\sin n\omega_0t \right\rangle=""",
            r"""0 \quad""",
            r"""\omega_0=\frac{2\pi}{T_0}""",
        ).to_edge(UP, buff=3.2)
        eq40 = MathTex(
            r"""1(t)\bot \sin n\omega_0t\Longleftrightarrow \left\langle 1,\sin n\omega_0t \right\rangle=0"""
        ).to_edge(UP, buff=5)
        self.play(
            TransformMatchingShapes(eq37[1], eq39[1]),
            TransformMatchingShapes(eq37[2], eq39[2]),
            TransformMatchingShapes(eq38, eq40),
        )
        self.wait(3)
        eq41 = MathTex(
            r"""\forall m,n\in \mathbb{Z}^+\quad""",
            r"""\left\langle 1,\cos n\omega_0t \right\rangle=""",
            r"""0 \quad""",
            r"""\omega_0=\frac{2\pi}{T_0}""",
        ).to_edge(UP, buff=3.2)
        eq42 = MathTex(
            r"""1(t)\bot \cos n\omega_0t\Longleftrightarrow \left\langle 1,\cos n\omega_0t \right\rangle=0"""
        ).to_edge(UP, buff=5)
        eq43 = MathTex(
            r"""\left\| 1(t) \right\|=\sqrt{\left\langle 1,1\right\rangle}=\sqrt{2}"""
        ).to_edge(UP, buff=6.2)
        self.play(
            TransformMatchingShapes(eq39[1], eq41[1]),
            TransformMatchingShapes(eq39[2], eq41[2]),
            TransformMatchingShapes(eq40, eq42),
            TransformMatchingShapes(eq36, eq43),
        )
        eq44 = MathTex(
            r"""\left\| \frac{1}{\sqrt{2}} \right\|=\sqrt{\left\langle \frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right\rangle}=1"""
        ).to_edge(UP, buff=6.2)
        self.wait(2)
        self.play(TransformMatchingShapes(eq43, eq44))
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(FadeOut(VGroup(eq29, eq34[:1], eq34[3:], eq41[1:3], eq42, eq44)))
        self.wait()
        eq45 = MathTex(
            r"""B=\left\{""",
            r"""\frac{1}{\sqrt{2}},\cos\omega_0t,...,\cos n\omega_0t,\sin\omega_0t ,...,\sin n\omega_0t""",
            r"""\right\}""",
            color=TEAL,
        ).to_edge(UP, buff=2.2)
        eq45[1].set_color(WHITE)
        self.play(Write(eq45))
        eq46 = Tex(
            r"""The set """,
            r"""$B$""",
            r""" is an""",
            r""" orthonormal basis """,
            r"""for the vector space\\ of square-integrable functions""",
        ).to_edge(UP, buff=3.9)
        eq46[1].set_color(TEAL)
        eq46[3].set_color(TEAL)
        self.play(Write(eq46))
        eq47 = MathTex(
            r"""\forall \mathbf{b}_i,\mathbf{b}_j\in B\quad\left\| \mathbf{b}_i \right\|=1\quad \left\langle  \mathbf{b}_i,\mathbf{b}_j\right\rangle=0\quad i\neq j"""
        ).to_edge(UP, buff=5.4)
        self.play(Write(eq47))
        eq48 = MathTex(
            r"""\forall x\in L^2\left(\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\right),\quad """,
            r"""x=\sum_{\mathbf{b}\in B}^{}\left\langle x,\mathbf{b} \right\rangle \mathbf{b}""",
        ).to_edge(UP, buff=6.4)
        self.play(Write(eq48))
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq49 = (
            MathTex(
                r"""x=\left\langle x,\frac{1}{\sqrt{2}}\right\rangle \frac{1}{\sqrt{2}} """,
                r"""+ \left\langle x,\cos\omega_0t \right\rangle
            \cos\omega_0t +\cdots + \left\langle x,\cos n\omega_0t \right\rangle \cos n\omega_0t+ \cdots""",
            )
            .to_edge(UP, buff=1.8)
            .scale(0.8)
        )
        eq50 = (
            Tex(
                r"""$$+ \left\langle x,\sin\omega_0t \right\rangle \sin\omega_0t +\cdots +
            \left\langle x,\sin n\omega_0t \right\rangle \sin n\omega_0t+\cdots$$"""
            )
            .to_edge(UP, buff=3)
            .scale(0.8)
        )
        self.play(
            FadeOut(VGroup(eq45, eq46, eq47, eq48[0])),
            TransformMatchingShapes(eq48[1], VGroup(eq49, eq50)),
        )
        self.wait(2)
        eq51 = (
            MathTex(
                r"""x=\frac{1}{2}\left\langle x,1 \right\rangle + \sum_{n=1}^{\infty}\left(\left\langle x,\cos n\omega_0t
            \right\rangle \cos n\omega_0t+\left\langle x,\sin n\omega_0t \right\rangle \sin n\omega_0t  \right)"""
            )
            .scale(0.8)
            .to_edge(UP, buff=2)
        )
        self.play(TransformMatchingShapes(VGroup(eq49, eq50), eq51))
        eq52 = (
            MathTex(
                r"""a_n=\left\langle x,\cos n\omega_0t \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\cos(n\omega_0t)dt"""
            )
            .scale(0.8)
            .to_edge(UP, buff=1.9 + 1.4 * 1)
        )
        eq53 = (
            MathTex(
                r"""a_0=\left\langle x,1 \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)dt"""
            )
            .scale(0.8)
            .to_edge(UP, buff=2 + 1.4 * 2)
        )
        eq54 = (
            MathTex(
                r"""b_n=\left\langle x,\sin n\omega_0t \right\rangle=\frac{2}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)\sin(n\omega_0t)dt"""
            )
            .scale(0.8)
            .to_edge(UP, buff=2 + 1.4 * 3)
        )
        self.wait()
        self.play(Write(VGroup(eq52, eq53, eq54)))
        self.wait(3)
        eq55 = (
            MathTex(
                r"""x(t)=\frac{a_0}{2} + \sum_{n=1}^{\infty}\left(a_n \cos n\omega_0t+b_n \sin n\omega_0t\right)""",
                color=TEAL_A,
            )
            .scale(0.8)
            .to_edge(UP, buff=2)
        )
        eq56 = (
            Title(
                r"""\textbf{Fourier Series}""",
                color=TEAL,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(
            TransformMatchingShapes(eq51, eq55), TransformMatchingShapes(eq21, eq56)
        )
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(FadeOut(VGroup(eq52, eq53, eq54, eq55, eq56)))
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": False},
            tips=False,
        )
        axes.add_coordinates()

        def series(N, x):
            terms = []
            for n in range(1, N + 1):
                b_n = (2 - 2 * (-1) ** n) / (PI * n)
                terms.append(b_n * math.sin(n * PI * x))
            return sum(terms)

        # Add axes and func
        self.play(Create(axes), run_time=5)
        self.wait()
        eq57 = (
            MathTex(
                r"""x(t)=\left\{\begin{matrix}-1&-1\le  t <0 \\ 0&t=0 \\ 1&0< t \le 1 \end{matrix}\right.\quad""",
                color=BLUE,
            )
            .scale(0.8)
            .to_corner(UL, buff=0.5)
        )
        dotf = Dot(ORIGIN, color=BLUE, z_index=4, radius=0.05)
        f1 = axes.plot(lambda x: -1, x_range=[-1, 0], color=BLUE)
        f2 = axes.plot(lambda x: 1, x_range=[0, 1], color=BLUE)
        self.play(Create(VGroup(f1, f2, dotf)), Write(eq57))
        self.wait()

        eq58 = (
            MathTex(
                r"""x(t)\approx \sum_{n=1}^{N} \frac{2-2(-1)^n}{\pi n}\sin n\pi t""",
                color=TEAL,
            )
            .scale(0.8)
            .to_corner(UR, buff=0.5)
        )
        self.wait()
        index1 = MathTex(f"n={1}", color=TEAL).scale(0.8).next_to(eq58, DOWN, buff=0.5)
        graph1 = axes.plot(lambda x: series(1, x), color=TEAL)
        self.play(Create(graph1), Write(eq58), Write(index1))
        self.wait()
        index = index1
        graph = graph1
        for N in range(3, 10, 2):
            index_new = (
                MathTex(f"n={N}", color=TEAL).scale(0.8).next_to(eq58, DOWN, buff=0.5)
            )
            graph_new = axes.plot(lambda x: series(N, x), color=TEAL)
            self.play(
                Transform(graph, graph_new), TransformMatchingShapes(index, index_new)
            )
            index = index_new
            self.wait()
        self.wait()

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(FadeOut(eq57, eq58, index, graph, dotf, f1, f2, axes))
        eq59 = (
            Title(
                r"""\textbf{Exponential Fourier Series}""",
                color=TEAL,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(Create(eq59))
        eq60 = (
            Tex(
                r"""We conclude that a Fourier series not only represents the function on the interval $\left[-\frac{T_0}{2},\frac{T_0}{2}\right]$ but also gives the periodic extension of the function outside this interval. The set """,
                r"""$\left\{ \frac{e^{jn\omega_0t}}{\sqrt{2}} \right\}_{n\in \mathbb{Z}}$""",
                r""" is also an orthonormal basis for the vector space $L^2$, this can be seen from """,
                r"""Euler's Formula: $e^{j\theta}=\cos\theta+j\sin\theta$""",
                color=WHITE,
            )
            .to_edge(UP, buff=1.7)
            .scale(0.75)
        )
        eq60[1].set_color(TEAL_A)
        eq60[3].set_color(TEAL_A)
        self.play(Write(eq60))
        eq61 = MathTex(
            r"""x(t)=\frac{a_0}{2} + \sum_{n=1}^{\infty}\left(a_n \cos n\omega_0t+b_n \sin n\omega_0t\right)""",
            color=WHITE,
        ).to_edge(UP, buff=4.2)
        self.play(Write(eq61))
        eq62 = MathTex(
            r"""x(t)=\frac{a_0}{2} + \sum_{n=1}^{\infty}\left(a_n \frac{e^{jn\omega_0t}+e^{-jn\omega_0t}}{2}
                +b_n \frac{e^{jn\omega_0t}-e^{-jn\omega_0t}}{2j}\right)""",
            color=WHITE,
        ).to_edge(UP, buff=4.2)
        self.play(TransformMatchingShapes(eq61, eq62))
        self.wait()
        eq63 = MathTex(
            r"""x(t)=\sum_{n=-\infty}^{\infty}\left(\frac{a_n}{2}-\frac{jb_n}{2}\right)e^{jn\omega_0t}""",
            color=WHITE,
        ).to_edge(UP, buff=4.2)
        self.play(TransformMatchingShapes(eq62, eq63))
        self.wait()
        eq64 = MathTex(
            r"""x(t)=\sum_{n=-\infty}^{\infty}D_ne^{jn\omega_0t}""",
            color=TEAL_A,
        ).to_edge(UP, buff=4.35)
        self.play(TransformMatchingShapes(eq63, eq64))
        eq65 = MathTex(
            r"""D_n=\frac{1}{2}\left\langle x,e^{jn\omega_0t}\right\rangle=\frac{1}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jn\omega_0t}dt""",
            color=TEAL_A,
        ).to_edge(UP, buff=5.9)
        self.play(Write(eq65))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq66 = (
            Title(
                r"""\textbf{Fourier Transform}""",
                color=TEAL,
            )
            .to_edge(UP, buff=0.9 - 0.2)
            .scale(1.1)
        )
        self.play(
            FadeOut(eq60, eq65),
            TransformMatchingShapes(eq59, eq66),
            eq64.animate.to_edge(UP, buff=2),
        )
        eq67 = MathTex(
            r"""\sum_{n=-\infty}^{\infty}\frac{1}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jn\omega_0t}dte^{jn\omega_0t}""",
            color=WHITE,
        ).to_edge(UP, buff=2 - 0.2)
        self.play(TransformMatchingShapes(eq64, eq67))
        eq68 = MathTex(
            r"""\sum_{n=-\infty}^{\infty}\frac{1}{2\pi}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jn\omega_0t}dte^{jn\omega_0t}\omega_0""",
            color=WHITE,
        ).to_edge(UP, buff=2 - 0.2)
        self.play(TransformMatchingShapes(eq67, eq68))
        eq69 = (
            Tex(
                r"""The Fourier series applies to periodic functions defined over the interval $\left[-\frac{T_0}{2},\frac{T_0}{2}\right]$. But the concept can be generalized to aperiodic functions defined over the entire real line, $t \in \mathbb{R}$, if we take the limit $T_0\to \infty$ carefully.""",
                color=WHITE,
            )
            .to_edge(UP, buff=3.7)
            .scale(0.75)
        )
        self.play(Write(eq69))
        eq70 = MathTex(
            r"""\lim_{T_0 \to \infty}\sum_{n=-\infty}^{\infty}\frac{1}{2\pi}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jn\omega_0t}dte^{jn\omega_0t}\omega_0""",
            color=WHITE,
        ).to_edge(UP, buff=2 - 0.2)
        self.play(TransformMatchingShapes(eq68, eq70))
        self.wait(3)
        eq71 = (
            Tex(
                r"""We therefore get the formulas for the """,
                r"""\textbf{Inverse and Forward Fourier Transfroms}""",
                r""" respectively:""",
                color=WHITE,
            )
            .to_edge(UP, buff=4 - 0.2)
            .scale(0.8)
        )
        eq71[1].set_color(TEAL)
        self.play(TransformMatchingShapes(eq69, eq71))
        eq72 = MathTex(
            r"""x(t)=\mathcal{F}^{-1}\left\{ X(j\omega) \right\}=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega""",
            color=TEAL_A,
        ).to_edge(UP, buff=5)
        eq73 = MathTex(
            r"""X(j\omega)=\mathcal{F}\left\{ x(t) \right\}=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}d\omega""",
            color=TEAL_A,
        ).to_edge(UP, buff=7 - 0.4)
        self.play(DrawBorderThenFill(VGroup(eq72, eq73)))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        self.play(FadeOut(eq66, eq70, eq71, eq72, eq73), FadeIn(plane))
        basis = self.get_basis_vectors()
        self.add(basis)
        vector = Vector([-3, -2], color=YELLOW)
        label_vector = self.get_vector_label(
            vector, Tex(r"$$\textbf{v}$$", color=YELLOW), direction=UP
        )
        self.add_vector(vector)
        self.play(FadeIn(label_vector))
        self.vector_to_coords(vector=vector)
        eq74 = Tex(
            r"""\textbf{Pythagorean theorem}""",
            color=YELLOW,
        ).to_edge(UP, buff=1)
        self.play(Write(eq74))
        eq75 = MathTex(
            r"""\mathbf{v}\cdot \mathbf{v}=\left\| \mathbf{v} \right\|^2 =(5)^2= (-3)^2+(-4)^2=(\mathbf{v}\cdot \mathbf{e}_1)^2+(\mathbf{v}\cdot \mathbf{e}_2)^2""",
            color=YELLOW,
        ).to_edge(UP, buff=2)
        self.play(Write(eq75))

        ####################################################################################################################

        self.next_section(skip_animations=Last)
        eq76 = MathTex(
            r"""\mathbf{v}\cdot \mathbf{v}=\left\| \mathbf{v} \right\|^2 =(\mathbf{v}\cdot \mathbf{e}_1)^2+(\mathbf{v}\cdot\mathbf{e}_2)^2""",
            color=TEAL_A,
        ).to_edge(UP, buff=2)
        self.play(
            FadeOut(plane, vector, basis, label_vector),
            TransformMatchingShapes(eq75, eq76),
            eq74.animate.set_color(TEAL),
        )
        eq77 = (
            Tex(
                r"""For any complete inner product space $V$ that has an orthonormal basis $B$""",
                color=WHITE,
            )
            .to_edge(UP, buff=3)
            .scale(0.8)
        )
        self.play(Write(eq77))
        eq78 = MathTex(
            r"""\forall \mathbf{v}\in V ,\quad\left\| \mathbf{v} \right\|^2 =\left\langle \mathbf{v},\mathbf{v} \right\rangle=\sum_{\mathbf{b}\in B}^{}\left| \left\langle \mathbf{v},\mathbf{b} \right\rangle \right|^2""",
            color=TEAL,
        ).to_edge(UP, buff=4)
        self.play(Write(eq78))
        eq79 = MathTex(
            r"""\forall x\in L^2\left(\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\right),\quad\left\| x \right\|^2 =\left\langle x,x \right\rangle=\sum_{n=-\infty}^{\infty}\left| \left\langle x,\frac{e^{jn\omega_0t}}{\sqrt{2}} \right\rangle \right|^2""",
            color=TEAL_A,
        ).to_edge(UP, buff=5.3)
        self.play(Write(eq79))
        self.wait()
        eq80 = MathTex(
            r"""\forall x\in L^2\left(\left[-\frac{T_0}{2},\frac{T_0}{2}\right]\right),\quad\left\| x \right\|^2 =\left\langle x,x \right\rangle=\sum_{n=-\infty}^{\infty}2\left| D_n \right|^2""",
            color=TEAL_A,
        ).to_edge(UP, buff=5.3)
        self.play(TransformMatchingShapes(eq79, eq80))
        self.wait()
        eq81 = MathTex(
            r"""\lim_{T_0 \to \infty} \frac{1}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}\left| x(t) \right|^2dt=\sum_{n=-\infty}^{\infty}\left| D_n \right|^2""",
            color=TEAL_A,
        ).to_edge(UP, buff=5.3)
        eq82 = Tex(
            r"""\textbf{Parseval's identity}""",
            color=TEAL,
        ).to_edge(UP, buff=1)
        self.play(TransformMatchingShapes(eq80, eq81), TransformMatchingTex(eq74, eq82))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=1)
        self.play(FadeOut(eq78, eq76, eq77, eq81, eq82))
        eq83 = (
            Tex(
                r"""Fin.""",
            )
            .scale(6)
            .set_color_by_gradient(TEAL, WHITE)
        )
        self.play(Write(eq83), run_time=6)
        self.wait(2)