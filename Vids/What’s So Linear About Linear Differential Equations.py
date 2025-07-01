from manim import *
import math

Skip = 1

class Linear(VectorScene):

    def construct(self):

        self.next_section(skip_animations=Skip)

        # Create a grid
        grid = NumberPlane()

        # Create a line and an equation
        graph1 = grid.plot(lambda x: 2 * x - 4, color=ORANGE, stroke_width=7)
        eq1 = (
            MathTex(
                r"""y=2x-4""",
                color=ORANGE,
            )
            .move_to([-4, 1.5, 0])
            .scale(1.5)
        )
        self.play(Create(grid))
        self.play(Create(graph1), Write(eq1))
        self.wait(1)

        # Transform into another line and equation
        graph2 = grid.plot(lambda x: -2 * x + 4, color=ORANGE, stroke_width=7)
        eq2 = (
            MathTex(
                r"""y=-2x+4""",
                color=ORANGE,
            )
            .move_to([-4, 1.5, 0])
            .scale(1.5)
        )
        self.play(TransformMatchingShapes(eq1, eq2), Transform(graph1, graph2))
        self.wait(1)

        # Transform into another line and equation
        graph3 = grid.plot(lambda x: 2 * x + 2, color=ORANGE, stroke_width=7)
        eq3 = (
            MathTex(
                r"""y=2x+2""",
                color=ORANGE,
            )
            .move_to([-4, 1.5, 0])
            .scale(1.5)
        )
        self.remove(eq1)
        self.remove(graph1)
        self.play(TransformMatchingShapes(eq2, eq3), Transform(graph2, graph3))
        self.wait(1)

        # Transform into another line and equation
        graph4 = grid.plot(lambda x: 2 * x, color=ORANGE, stroke_width=7)
        eq4 = (
            MathTex(
                r"""y=2x""",
                color=ORANGE,
            )
            .move_to([-4, 1.5, 0])
            .scale(1.5)
        )
        self.remove(eq2)
        self.remove(graph2)
        self.play(TransformMatchingShapes(eq3, eq4), Transform(graph3, graph4))
        self.wait(1)

        # Changing slopes of a linear function
        for a in [0.5, 3, -2]:
            graph5 = grid.plot(lambda x: a * x, color=ORANGE, stroke_width=7)
            eq5 = (
                MathTex(
                    f"y={a}x",
                    color=ORANGE,
                )
                .move_to([-4, 1.5, 0])
                .scale(1.5)
            )
            self.remove(graph3)
            if a == 0.5:
                self.remove(eq3)
                self.play(TransformMatchingShapes(eq4, eq5), Transform(graph4, graph5))
            elif a == 3:
                self.remove(eq4)
                self.play(TransformMatchingShapes(eqs, eq5), Transform(graph4, graph5))
            elif a == -2:
                self.remove(eq5)
                self.play(TransformMatchingShapes(eqs, eq5), Transform(graph4, graph5))
            eqs = eq5
            self.wait(1)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Next scene animation
        eq6 = (
            MathTex(
                "y=ax",
                color=WHITE,
            )
            .move_to([0, 1.5, 0])
            .scale(1.5)
        )
        self.play(FadeOut(grid, graph4), TransformMatchingShapes(eq5, eq6))
        self.wait(1)

        # Linear function properties
        eq7 = (
            MathTex(
                "f(x)=ax",
                color=WHITE,
            )
            .move_to([0, 1.5, 0])
            .scale(1.5)
        )
        self.remove(eq5)
        self.play(TransformMatchingShapes(eq6, eq7))
        eq8 = MathTex(
            r"""\\1.\quad f(u+v)=a(u+v)=au+av=f(u)+f(v)""",
            color=WHITE,
        ).move_to([0, 0.5, 0])
        self.play(Write(eq8))
        self.wait(1)
        eq9 = MathTex(
            r"""\\2. \quad f(cu)=acu=c(au)=cf(u)""",
            color=WHITE,
        ).move_to([0, -0.5, 0])
        self.play(Write(eq9))
        self.wait(1)
        eq10 = MathTex(
            r"""\\f:\mathbb{R}\longrightarrow    \mathbb{R}""",
            color=WHITE,
        ).move_to([0, -1.5, 0])
        self.play(Write(eq10))
        self.wait(2)

        # Linear function from R^2 to R
        eq11 = (
            MathTex(
                r"""f(x,y)=ax+by""",
                color=WHITE,
            )
            .move_to([0, 1.5, 0])
            .scale(1.5)
        )
        eq12 = MathTex(
            r"""\\1.\quad f(\textbf{u}+\textbf{v})=f(\textbf{u})+f(\textbf{v})""",
            color=WHITE,
        ).move_to([0, 0.5, 0])
        eq13 = MathTex(
            r"""\\2. \quad f(c\textbf{u})=cf(\textbf{u})""",
            color=WHITE,
        ).move_to([0, -0.5, 0])
        eq14 = MathTex(
            r"""\\f:\mathbb{R}^2\longrightarrow    \mathbb{R}""",
            color=WHITE,
        ).move_to([0, -1.5, 0])
        self.play(
            TransformMatchingShapes(eq7, eq11),
            TransformMatchingShapes(eq8, eq12),
            TransformMatchingShapes(eq9, eq13),
            TransformMatchingShapes(eq10, eq14),
        )
        self.wait(1)


class Linear1(ThreeDScene):

    def construct(self):

        # ThreeD plane scene
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u + v),
            u_range=[-3, 3],
            v_range=[-3, 3],
            checkerboard_colors=[PURPLE_E, PURPLE_E],
        )
        self.add(axes, surface)
        self.play(Write(MathTex("f(x,y)=x+y").to_corner(UL, buff=1)))
        self.begin_ambient_camera_rotation(rate=PI / 20)
        self.wait(5)
        self.stop_ambient_camera_rotation()


class Linear2(Scene):

    def construct(self):

        self.next_section(skip_animations=Skip)

        eq15 = (
            Title(
                r"""\textbf{Linear Map}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(Write(eq15))
        eq16 = (
            Tex(
                r"""A linear map (also called a linear transformation, or """,
                r"""vector space""",
                r""" homomorphism) is a mapping } $V\to  W$ between two vector spaces that preserves 
                the operations of vector addition and scalar multiplication}""",
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        self.play(Write(eq16))
        eq17 = (
            BulletedList(
                r"""$f(\textbf{u}+\textbf{v})=f(\textbf{u})+f(\textbf{v})$""",
                r"""$f(c\textbf{u})=cf(\textbf{u})$""",
            )
            .scale(1.3)
            .to_edge(UP, buff=4.6)
            .set_color(PURPLE_A)
        )
        self.play(Write(eq17))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # vector space
        eq18 = (
            Tex(
                r"""vector space""",
                color=ORANGE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(TransformMatchingTex(eq16, eq18), FadeOut(VGroup(eq15, eq17)))
        self.wait(1)

        # Definition of a vector space
        eq19 = (
            Tex(
                r"""A linear space is a set whose elements, often called vectors, may be added 
                together and multiplied ("scaled") by numbers called scalars"""
            )
            .to_edge(UP, buff=1.5)
            .scale(0.8)
        )
        self.play(Write(eq19))
        self.wait()

        # Examples of vector spaces - Arrows
        rec1 = RoundedRectangle(
            corner_radius=0.2,
            width=3.8,
            height=4,
            stroke_color=color_gradient([ORANGE, PURPLE], 10),
            stroke_width=10,
        ).move_to([-4.3, -1, 0])
        start_point = [-4.4, -1.2, 0]
        count = 0
        vectors = VGroup()
        for shift in [
            [1, 1, 0],
            [1.5, 0.1, 0],
            [0.5, -0.5, 0],
            [0.5, -1, 0],
            [-0.8, -1.3, 0],
            [-0.3, -1, 0],
            [-1.2, -0.5, 0],
            [-0.8, 0.5, 0],
            [-0.4, 1, 0],
        ]:
            count += 1
            end_point = [sum(x) for x in zip(start_point, shift)]
            vector = Line(
                start=start_point,
                end=end_point,
                color=ORANGE if count % 2 == 0 else PURPLE,
            ).add_tip(tip_width=0.2, tip_length=0.3)
            vectors += vector
        vectors_word = Tex("Arrows").move_to([-4.3, 0.47, 0])
        self.play(Create(vectors), Write(vectors_word))
        self.play(Create(rec1))
        self.wait(1)

        # Examples of vector spaces - Lists
        rec2 = RoundedRectangle(
            corner_radius=0.2,
            width=3.8,
            height=4,
            stroke_color=color_gradient([ORANGE, PURPLE], 10),
            stroke_width=10,
        ).move_to([0, -1, 0])
        lists = VGroup()
        for list in [
            [-4, 7, [-1, -0.6, 0]],
            [-2, 5, [0, -0.6, 0]],
            [-5, 5, [1, -0.6, 0]],
            [8, -7, [-1, -1.8, 0]],
            [8, -6, [0, -1.8, 0]],
            [3, -1, [1, -1.8, 0]],
        ]:
            count += 1
            string = (
                r"""\begin{bmatrix}"""
                + str(list[0])
                + r"""\\"""
                + str(list[1])
                + r"""\end{bmatrix}"""
            )
            lists += (
                MathTex(string)
                .move_to(list[2])
                .scale(0.8)
                .set_color(ORANGE if count % 2 == 0 else PURPLE)
            )
        lists_word = Tex("Lists").move_to([0, 0.47, 0])
        self.play(Create(lists), Write(lists_word))
        self.play(Create(rec2))
        self.wait(1)

        # Examples of vector spaces - Functions
        rec3 = RoundedRectangle(
            corner_radius=0.2,
            width=3.8,
            height=4,
            stroke_color=color_gradient([ORANGE, PURPLE], 10),
            stroke_width=10,
        ).move_to([4.3, -1, 0])
        axes = Axes(x_length=3.8, y_length=3, tips=False, x_range=[-5, 5]).move_to(
            [4.3, -1.5, 0]
        )
        fn1 = axes.plot(
            lambda x: -1 * (x - 1) ** 2 + 2, x_range=[-1.449, 3.449]
        ).set_color(ORANGE)
        fn2 = axes.plot(
            lambda x: (x + 1) ** 3 - 3 * (x + 1), x_range=[-3.196, 1.196]
        ).set_color(PURPLE)
        fns_word = Tex("Functions").move_to([4.3, 0.47, 0])
        self.play(Create(VGroup(axes, fn1, fn2)), Write(fns_word))
        self.play(Create(rec3))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Function Spaces
        eq20 = (
            Title(
                r"""\textbf{Function Space}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        eq21 = (
            Tex(
                r"""A function space is a vector space of functions\\that all have the same domain and codomain""",
            )
            .to_edge(UP, buff=2.3)
            .scale(0.8)
            .to_edge(LEFT, buff=0.7)
        )
        self.play(
            FadeOut(
                VGroup(vectors_word, lists_word, eq19, rec1, rec2, vectors, lists, eq18)
            ),
            Write(eq20),
        )
        self.play(Write(eq21))
        eq22 = (
            BulletedList(
                r"""$(f+g)(x)=f(x)+g(x)$""",
                r"""$(c\cdot f)(x)=c\cdot f(x)$""",
            )
            .scale(1.3)
            .to_edge(UP, buff=4.4)
            .to_edge(LEFT, buff=0.7)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(Write(eq22))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Title
        eq23 = (
            Tex(
                r"""Differentiation is a map""",
                color=ORANGE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )

        # Tracker variable
        p = ValueTracker(0)

        # Define stuff
        eq24 = (
            MathTex(r"""\frac{d }{dx}""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        axes1 = (
            Axes(x_length=2.6, y_length=4, tips=False, x_range=[0, 2 * PI])
            .move_to([-4, -1, 0])
            .set_color(BLACK)
        )
        axes2 = (
            Axes(x_length=2.6, y_length=4, tips=False, x_range=[0, 2 * PI])
            .move_to([4, -1, 0])
            .set_color(BLACK)
        )
        graph_sin = axes1.plot(lambda x: math.sin(x), x_range=[0, 2 * PI])
        graph_cos = always_redraw(
            lambda: axes2.plot(lambda x: math.cos(x), x_range=[0, p.get_value()])
        )
        slope = always_redraw(
            lambda: axes1.plot(
                lambda x: math.cos(p.get_value()) * (x - p.get_value())
                + math.sin(p.get_value()),
                x_range=[
                    p.get_value() - 1.5 * math.cos(math.cos(p.get_value())),
                    p.get_value() + 1.5 * math.cos(math.cos(p.get_value())),
                ],
            ).set_color(ORANGE)
        )
        dot = always_redraw(
            lambda: Dot().move_to(axes1.c2p(p.get_value(), math.sin(p.get_value())))
        )

        # Play animations
        self.play(
            FadeOut(VGroup(rec3, axes, fn1, fn2, eq22, eq21, eq20, fns_word)),
            Write(eq23),
        )
        self.play(Create(VGroup(axes1, axes2, graph_sin, graph_cos, slope, dot)))
        domain = Circle(
            radius=2, stroke_color=color_gradient([ORANGE, PURPLE], 10), stroke_width=10
        ).move_to([-4, -1, 0])
        codomain = Circle(
            radius=2, stroke_color=color_gradient([ORANGE, PURPLE], 10), stroke_width=10
        ).move_to([4, -1, 0])
        self.play(Create(VGroup(domain, codomain)))
        arrow = Line([-1.4, -1, 0], [1.4, -1, 0]).add_tip(tip_shape=StealthTip)
        self.play(Create(arrow), Write(eq24))
        self.play(p.animate.set_value(2 * PI), run_time=5)
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Title
        eq25 = (
            Tex(
                r"""Differentiation is a linear map""",
                color=ORANGE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )

        # Differentiation is a linear map
        eq26 = (
            MathTex(
                r"""\frac{d }{dx}(af(x)+bg(x))=a\frac{d f(x)}{dx}+b\frac{d g(x)}{dx}"""
            )
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )

        # Transform animation
        self.remove(VGroup(axes1, axes2))
        self.play(
            FadeOut(VGroup(domain, codomain, graph_cos, graph_sin, slope, dot, arrow)),
            TransformMatchingShapes(eq23, eq25),
            TransformMatchingShapes(eq24, eq26),
        )
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Differentiation Operator
        eq27 = (
            MathTex(r"""\frac{d }{dx}=D""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(TransformMatchingShapes(eq26, eq27))
        eq28 = MathTex(r"""D(f+g)=(Df)+(Dg)\qquad D(af)=a(Df)""").move_to([0, -2, 0])
        self.play(Write(eq28))
        self.wait(1)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Constructing a general Linear Differential Operator
        eq29 = (
            MathTex(r"""L=D""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        eq30 = MathTex(r"""L(f+g)=(Lf)+(Lg)\qquad L(af)=a(Lf)""").move_to([0, -2, 0])
        self.play(
            TransformMatchingShapes(eq27, eq29), TransformMatchingShapes(eq28, eq30)
        )
        self.wait(1)
        eq31 = (
            MathTex(r"""L=a_1(x)D""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(TransformMatchingShapes(eq29, eq31))
        self.wait(1)
        eq32 = (
            MathTex(r"""L=a_1(x)D+a_0(x)""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(TransformMatchingShapes(eq31, eq32))
        self.wait(1)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        eq33 = (
            MathTex(
                r"""L=a_n(x)D^n+a_{n-1}(x)D^{n-1}+\cdots +a_{2}(x)D^{2}+a_{1}(x)D+a_{0}(x)"""
            )
            .move_to([0, -0.5, 0])
            .scale(0.9)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(FadeOut(eq25), TransformMatchingShapes(eq32, eq33))
        eq34 = (
            Title(
                r"""\textbf{Linear Differential Operator}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(Write(eq34))
        eq35 = (
            Tex(
                r"""A differential operator is an operator defined as a function of the differentiation operator. An $n$th-order 
                differential operator that \\possesses a linearity property is called a linear differential operator."""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        self.play(Write(eq35))
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        eq36 = (
            Title(
                r"""\textbf{Linear Differential Equation}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        eq37 = (
            Tex(
                r"""A linear differential equation is a differential equation that \\is defined 
                by a linear polynomial in the unknown function \\and its derivatives, that is an equation of the form:"""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        eq38 = (
            MathTex(
                r"""a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+\cdots +a_{2}(x)y''+a_{1}(x)y'+a_{0}(x)y=b(x)"""
            )
            .move_to([0, -0.5, 0])
            .scale(0.9)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        eq39 = MathTex(r"""L(y(x))=b(x)""").move_to([0, -2, 0])
        self.play(
            TransformMatchingShapes(eq30, eq39),
            TransformMatchingShapes(eq35, eq37),
            TransformMatchingShapes(eq34, eq36),
            TransformMatchingShapes(eq33, eq38),
        )
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        eq40 = (
            Title(
                r"""\textbf{Homogeneous Linear Differential Equation}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        eq41 = (
            Tex(r"""What function does the linear differential operator map to zero?""")
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        eq42 = (
            MathTex(
                r"""a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+\cdots +a_{2}(x)y''+a_{1}(x)y'+a_{0}(x)y=0"""
            )
            .move_to([0, -0.5, 0])
            .scale(0.9)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        eq43 = MathTex(r"""L(y(x))=0""").move_to([0, -2, 0])
        self.play(
            TransformMatchingShapes(eq39, eq43),
            TransformMatchingShapes(eq37, eq41),
            TransformMatchingShapes(eq36, eq40),
            TransformMatchingShapes(eq38, eq42),
        )
        self.wait(1)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Introduce the kernel
        eq44 = (
            Tex(
                r"""What is the """,
                r"""kernel""",
                r""" of the linear differential operator?""",
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        eq44[1].set_color(ORANGE)
        eq45 = MathTex(
            r"""\text{ker}(L)=\left\{ y\in C^n(I)|L(y)=0 \right\}=L^{-1}(0)"""
        ).move_to([0, -2, 0])
        self.play(
            TransformMatchingShapes(eq41, eq44), TransformMatchingShapes(eq43, eq45)
        )
        self.wait(5)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # kernel
        eq46 = (
            Tex(
                r"""kernel""",
                color=ORANGE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(FadeOut(VGroup(eq40, eq42, eq45)), TransformMatchingTex(eq44, eq46))

        # Definition of a kernel
        eq47 = (
            Tex(
                r"""The kernel of a linear map, also known as the nullspace, is the  linear subspace 
                of the domain which the map maps to the zero vector"""
            )
            .to_edge(UP, buff=1.5)
            .scale(0.8)
        )
        self.play(Write(eq47))
        self.wait()

        # Mapping animation
        self.play(Create(VGroup(domain, codomain)))
        domain_label = (
            MathTex(r"""C^n(I)""")
            .next_to(domain, DR, buff=0)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        codomain_label = (
            MathTex(r"""C(I)""")
            .next_to(codomain, DL, buff=0)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(Write(VGroup(domain_label, codomain_label)))
        kernel = (
            Circle(radius=1, color=ORANGE, fill_opacity=1)
            .move_to([-4, -1, 0])
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        kernel_label = MathTex(r"""\text{ker}(L)""").move_to([-4, -1, 0])
        kernel_group = VGroup(kernel, kernel_label)
        zero_vector = Dot().move_to([4, -1, 0])
        zero_vector_label = Tex("0").next_to(zero_vector, RIGHT)
        self.play(Create(VGroup(kernel, kernel_label)))
        arrow = Line([-1.4, -1, 0], [1.4, -1, 0]).add_tip(tip_shape=StealthTip)
        eq48 = (
            MathTex(r"""L""")
            .move_to([0, 0.5, 0])
            .scale(1.5)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(Create(arrow), Write(eq48))
        self.play(
            TransformFromCopy(kernel_group, zero_vector), Write(zero_vector_label)
        )
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Linear Independence
        eq49 = (
            Title(
                r"""\textbf{Linear Independence}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        self.play(
            FadeOut(
                VGroup(
                    eq46,
                    eq47,
                    eq48,
                    arrow,
                    domain,
                    codomain,
                    domain_label,
                    codomain_label,
                    kernel_group,
                    zero_vector,
                    zero_vector_label,
                )
            ),
            Write(eq49),
        )
        eq50 = (
            Tex(
                r"""A set of vectors is said to be linearly independent if there exists no \\nontrivial 
                linear combination of the vectors that equals the zero vector."""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        eq51 = (
            MathTex(
                r"""c_1f_1+c_2f_2+\cdots +c_nf_n=0\Longrightarrow c_1=c_2=\cdots =c_n=0"""
            )
            .scale(1)
            .to_edge(UP, buff=3.4)
            .set_color(PURPLE_A)
        )
        self.play(Write(VGroup(eq50, eq51)))
        self.wait(1)
        eq52 = (
            MathTex(r"""c_1f_1+c_2f_2+\cdots +c_nf_n=0""")
            .scale(1)
            .to_edge(UP, buff=3.4)
            .set_color(PURPLE_A)
        )
        self.play(TransformMatchingShapes(eq51, eq52))
        eq53 = (
            MathTex(r"""c_1f_1'+c_2f_2'+\cdots +c_nf_n'=0""")
            .scale(1)
            .to_edge(UP, buff=4.2)
            .set_color(PURPLE_A)
        )
        self.play(TransformFromCopy(eq52, eq53))
        eq54 = (
            MathTex(r"""c_1f_1''+c_2f_2''+\cdots +c_nf_n''=0""")
            .scale(1)
            .to_edge(UP, buff=5)
            .set_color(PURPLE_A)
        )
        self.play(TransformFromCopy(eq53, eq54))
        vertical_dots = MathTex(r"""\vdots""").to_edge(UP, buff=5.8).set_color(PURPLE_A)
        self.play(Write(vertical_dots))
        eq55 = (
            MathTex(r"""c_1f_1^{(n-1)}+c_2f_2^{(n-1)}+\cdots +c_nf_n^{(n-1)}=0""")
            .scale(1)
            .to_edge(UP, buff=6.6)
            .set_color(PURPLE_A)
        )
        self.play(TransformFromCopy(eq54, eq55))
        equations = VGroup(eq52, eq53, eq54, vertical_dots, eq55)
        eq56 = (
            MathTex(
                r"""\left[ \begin{matrix}
                f_1 & f_2 & \cdots  &  f_n\\f_1' & f_2' & \cdots&  f_n'\\
                f_1'' & f_2'' & \cdots&  f_n''\\\vdots  & \vdots  & \ddots  & \vdots  \\
                f_1^{(n-1)} & f_2^{(n-1)} & \cdots&  f_n^{(n-1)}\end{matrix}  \right]\left[ \begin{matrix}c_1 \\
                c_2 \\\vdots  \\c_{n} \end{matrix} \right]=\left[ \begin{matrix}
                0 \\0 \\0  \\\vdots \\0\end{matrix} \right]"""
            )
            .scale(1)
            .to_edge(UP, buff=3.8)
            .set_color(PURPLE_A)
        )
        self.play(TransformMatchingShapes(equations, eq56))
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # The Wronskian
        eq57 = (
            MathTex(
                r"""W(f_1,f_2,\cdots ,f_n)(x)=\left| \begin{matrix}
                    f_1(x) & f_2(x) & \cdots  &  f_n(x)\\
                    f_1'(x) & f_2'(x) & \cdots&  f_n'(x)\\
                    f_1''(x) & f_2''(x) & \cdots&  f_n''(x)\\
                    \vdots  & \vdots  & \ddots  & \vdots  \\
                    f_1^{(n-1)}(x) & f_2^{(n-1)}(x) & \cdots&  f_n^{(n-1)}(x)
                    \end{matrix}  \right|"""
            )
            .scale(1)
            .to_edge(UP, buff=3.8)
            .set_color(PURPLE_A)
        )
        eq58 = (
            Title(
                r"""\textbf{Wronskian}""",
                color=PURPLE,
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        eq59 = (
            Tex(
                r"""The Wronskian of $n$ differentiable functions is the determinant \\formed with the
                functions and their derivatives up to order $n - 1$."""
            )
            .to_edge(UP, buff=2)
            .scale(0.9)
        )
        self.play(
            TransformMatchingShapes(eq56, eq57),
            TransformMatchingShapes(eq49, eq58),
            TransformMatchingShapes(eq50, eq59),
        )
        self.wait(1)
        eq60 = (
            MathTex(
                r"""W(f_1,f_2,\cdots ,f_n)(x)\neq 0 \Longrightarrow \text{linear independence}"""
            )
            .scale(1)
            .to_edge(UP, buff=3.8)
            .set_color(PURPLE_A)
        )
        self.play(TransformMatchingShapes(eq57, eq60))
        self.wait(2)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # A basis for the kernel of L
        self.play(FadeOut(VGroup(eq58, eq59, eq60)))
        eq61 = (
            Tex(
                r"""If """,
                r"""$y_1,y_2,\cdots,y_n$""",
                r""" are """,
                r"""$n$""",
                r""" linearly independent solutions of """,
                r"""$L(y)=0$""",
                r""", then the linear 
                combination """,
                r"""$c_1y_1+c_2y_2+\cdots+c_ny_n$""",
                r""" where """,
                r"""$c_1,c_2,\cdots,c_n$""",
                r""" are scalars, is also a solution, 
                we call the set """,
                r"""$\left\{ y_1,y_2,\cdots,y_n \right\}$""",
                r""" a fundamental set of solutions of the homogeneous 
                linear """,
                r"""$n$""",
                r"""th-order differential equation""",
            )
            .to_edge(UP, buff=1)
            .scale(0.8)
        )
        eq61[1].set_color_by_gradient(ORANGE, PURPLE)
        eq61[3].set_color_by_gradient(ORANGE, PURPLE)
        eq61[5].set_color_by_gradient(ORANGE, PURPLE)
        eq61[7].set_color_by_gradient(ORANGE, PURPLE)
        eq61[9].set_color_by_gradient(ORANGE, PURPLE)
        eq61[11].set_color_by_gradient(ORANGE, PURPLE)
        eq61[13].set_color_by_gradient(ORANGE, PURPLE)
        self.play(Write(eq61))
        self.wait(2)
        eq62 = (
            MathTex(
                r"""\text{span}\left\{ y_1,y_2,\cdots,y_n \right\}=\text{ker}(L)\\\text{Nullity}(L)=\text{dim}(\text{ker}(L))=n"""
            )
            .to_edge(UP, buff=4.6)
            .scale(1.8)
        )
        eq62.set_color_by_gradient(ORANGE, PURPLE)
        self.play(Write(eq62))
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        # Solve an example of a linear differential equation
        self.play(FadeOut(VGroup(eq61, eq62)))
        eq64 = (
            Tex(
                r"""Solve the linear differential equation: $\frac{d^2 y}{dx^2}-5\frac{d y}{dx}+6y=0$"""
            )
            .to_edge(UP, buff=0.9)
            .scale(1.1)
        )
        eq64.set_color_by_gradient(ORANGE, PURPLE)
        eq65 = (
            MathTex(r"""\frac{d^2 y}{dx^2}-5\frac{d y}{dx}+6y=0""")
            .to_edge(UP, buff=4)
            .scale(1.5)
        )
        eq66 = MathTex(r"""D^2y-5Dy+6y=0""").to_edge(UP, buff=4).scale(1.5)
        eq67 = MathTex(r"""(D^2-5D+6)y=0""").to_edge(UP, buff=4).scale(1.5)
        eq68 = MathTex(r"""(D^2-5D+6)e^{\lambda x}=0""").to_edge(UP, buff=4).scale(1.5)
        eq69 = (
            MathTex(r"""(\lambda^2-5\lambda+6)e^{\lambda x}=0""")
            .to_edge(UP, buff=4)
            .scale(1.5)
        )
        eq70 = MathTex(r"""(\lambda^2-5\lambda+6)=0""").to_edge(UP, buff=4).scale(1.5)
        eq71 = MathTex(r"""(\lambda-2)(\lambda-3)=0""").to_edge(UP, buff=4).scale(1.5)
        eq72 = MathTex(r"""\lambda_1=2,\lambda_2=3""").to_edge(UP, buff=4).scale(1.5)
        eq73 = MathTex(r"""y_1=e^{2x},y_2=e^{3x}""").to_edge(UP, buff=4).scale(1.5)
        eq74 = (
            MathTex(
                r"""W(e^{2x},e^{3x})=\begin{vmatrix}
                    e^{2x} &e^{3x}  \\
                    2e^{2x} &3e^{3x} 
                    \end{vmatrix}"""
            )
            .to_edge(UP, buff=4)
            .scale(1.5)
        )
        eq75 = (
            MathTex(r"""W(e^{2x},e^{3x})=3e^{5x}-2e^{5x}""")
            .to_edge(UP, buff=4)
            .scale(1.5)
        )
        eq76 = MathTex(r"""W(e^{2x},e^{3x})\neq 0""").to_edge(UP, buff=4).scale(1.5)
        eq77 = (
            MathTex(r"""(D^2-5D+6)(c_1e^{2x}+c_2e^{3x})=0""")
            .to_edge(UP, buff=4)
            .scale(1.5)
        )
        eq78 = MathTex(r"""y=c_1e^{2x}+c_2e^{3x}""").to_edge(UP, buff=4).scale(1.5)
        self.play(Write(eq64))
        self.wait(1)
        self.play(Write(eq65))
        self.wait(2)
        self.play(TransformMatchingShapes(eq65, eq66))
        self.wait(2)
        self.play(TransformMatchingShapes(eq66, eq67))
        self.wait(2)
        self.play(TransformMatchingShapes(eq67, eq68))
        self.wait(2)
        self.play(TransformMatchingShapes(eq68, eq69))
        self.wait(2)
        self.play(TransformMatchingShapes(eq69, eq70))
        self.wait(2)
        self.play(TransformMatchingShapes(eq70, eq71))
        self.wait(2)
        self.play(TransformMatchingShapes(eq71, eq72))
        self.wait(2)
        self.play(TransformMatchingShapes(eq72, eq73))
        self.wait(2)
        self.play(TransformMatchingShapes(eq73, eq74))
        self.wait(2)
        self.play(TransformMatchingShapes(eq74, eq75))
        self.wait(2)
        self.play(TransformMatchingShapes(eq75, eq76))
        self.wait(2)
        self.play(TransformMatchingShapes(eq76, eq77))
        self.wait(2)
        self.play(TransformMatchingShapes(eq77, eq78))
        self.wait(2)
        eq79 = (
            MathTex(
                r"""\text{span}\left\{e^{2x},e^{3x}\right\}=\text{ker}(D^2-5D+6)""",
                color=PURPLE_A,
            )
            .to_edge(UP, buff=6)
            .scale(1.5)
        )
        self.play(Write(eq79))
        self.wait(1)

        ####################################################################################################################

        self.next_section(skip_animations=Skip)

        self.play(FadeOut(VGroup(eq64, eq78, eq79)))
        eq80 = (
            Tex(
                r"""Linear differential equations\\ are those which can be\\ reduced to the form $Ly=b$, \\where $L$ is some linear operator."""
            )
            .to_edge(UP, buff=2.8)
            .scale(1.5)
        )    
        eq80.set_color_by_gradient(ORANGE, PURPLE)    
        self.play(Write(eq80))        
        self.wait(3)

        ####################################################################################################################

        self.next_section(skip_animations=0)
        self.play(FadeOut(eq80))
        eq81 = (
            Tex(
                r"""Fin.""",
            )
            .scale(6)
            .set_color_by_gradient(ORANGE, PURPLE)
        )
        self.play(Write(eq81), run_time=6)
        self.wait(2)
