from manim import *

class QRDecompositionScene(Scene):
    def construct(self):
        # Define colors for consistent use throughout the animation
        a_color = BLUE
        q_color = GREEN
        r_color = ORANGE
        
        #####################################
        # Section 1: Introduction (0-3s)
        #####################################
        
        # Create matrix A and display it
        matrix_a = MathTex(
            "A = \\begin{bmatrix} 3 & 1 \\\\ 2 & 2 \\end{bmatrix}",
            color=a_color
        ).scale(1.2)
        
        # Show matrix A appearing in the center
        self.play(Write(matrix_a), run_time=1)
        self.wait(0.5)
        
        # Create the QR decomposition equation
        eq_left = MathTex("A", color=a_color).scale(1.2)
        eq_equals = MathTex("=").scale(1.2)
        eq_q = MathTex("Q", color=q_color).scale(1.2)
        eq_times = MathTex("\\times").scale(1.2)
        eq_r = MathTex("R", color=r_color).scale(1.2)
        
        equation = VGroup(eq_left, eq_equals, eq_q, eq_times, eq_r).arrange(RIGHT, buff=0.2)
        
        # Transform matrix A into the equation
        self.play(
            TransformMatchingTex(matrix_a, equation),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Add subtitle
        subtitle = Text("QR Decomposition: Breaking down a matrix", font_size=32)
        subtitle.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(0.5)
        
        #####################################
        # Section 2: Matrix A as transformation (3-4s)
        #####################################
        
        # Move equation to the top
        self.play(
            equation.animate.to_edge(UP, buff=0.5),
            FadeOut(subtitle),
            run_time=1
        )
        
        # Create coordinate grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        # Create the standard basis vectors
        e1 = Arrow(grid.c2p(0, 0), grid.c2p(1, 0), color=WHITE, buff=0)
        e2 = Arrow(grid.c2p(0, 0), grid.c2p(0, 1), color=WHITE, buff=0)
        standard_basis = VGroup(e1, e2)
        standard_basis_label = Text("Standard Basis", font_size=24).next_to(standard_basis, DOWN, buff=0.5)
        
        # Create the transformed basis vectors (columns of A)
        a1 = Arrow(grid.c2p(0, 0), grid.c2p(3, 2), color=a_color, buff=0)
        a2 = Arrow(grid.c2p(0, 0), grid.c2p(1, 2), color=a_color, buff=0)
        a_basis = VGroup(a1, a2)
        a_basis_label = Text("A transforms basis vectors", font_size=24).next_to(a_basis, DOWN, buff=0.5)
        
        # Show the grid and standard basis
        self.play(
            Create(grid),
            Create(standard_basis),
            FadeIn(standard_basis_label),
            run_time=1
        )
        self.wait(0.5)
        
        # Transform standard basis to A-transformed basis
        self.play(
            ReplacementTransform(e1.copy(), a1),
            ReplacementTransform(e2.copy(), a2),
            FadeOut(standard_basis_label),
            FadeIn(a_basis_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        #####################################
        # Section 3: Matrix Q visualization (4-6s)
        #####################################
        
        # Clear A transformation to introduce Q
        self.play(
            FadeOut(a_basis),
            FadeOut(a_basis_label),
            run_time=0.5
        )
        
        # Create the Q matrix
        q_matrix = MathTex(
            "Q = \\begin{bmatrix} 0.83 & -0.55 \\\\ 0.55 & 0.83 \\end{bmatrix}",
            color=q_color
        ).scale(1).to_edge(LEFT, buff=0.5)
        
        # Create Q orthogonal basis vectors
        q1 = Arrow(grid.c2p(0, 0), grid.c2p(0.83, 0.55), color=q_color, buff=0)
        q2 = Arrow(grid.c2p(0, 0), grid.c2p(-0.55, 0.83), color=q_color, buff=0)
        q_basis = VGroup(q1, q2)
        
        # Create right angle symbol to show orthogonality
        right_angle = Elbow(width=0.3, angle=0, color=WHITE).move_to(
            grid.c2p(0.25, 0.25)
        ).rotate(
            angle=np.arctan2(0.55, 0.83),
            about_point=grid.c2p(0, 0)
        )
        
        q_basis_label = Text("Q: Orthogonal Matrix", font_size=30, color=q_color)
        q_basis_label.to_edge(DOWN, buff=0.75)
        
        # Display Q matrix and its geometric interpretation
        self.play(
            Write(q_matrix),
            run_time=1
        )
        
        self.play(
            Create(q1),
            Create(q2),
            run_time=1
        )
        
        self.play(
            Create(right_angle),
            FadeIn(q_basis_label),
            run_time=0.5
        )
        
        orthogonal_prop = Text("Perpendicular unit vectors", font_size=24).next_to(q_basis_label, DOWN, buff=0.2)
        self.play(FadeIn(orthogonal_prop), run_time=0.5)
        self.wait(1)
        
        #####################################
        # Section 4: Matrix R visualization (6-8s)
        #####################################
        
        # Clear Q visualization
        self.play(
            FadeOut(q1),
            FadeOut(q2),
            FadeOut(right_angle),
            FadeOut(q_matrix),
            FadeOut(q_basis_label),
            FadeOut(orthogonal_prop),
            run_time=0.5
        )
        
        # Create R matrix with highlighted structure
        r_matrix_template = "R = \\begin{bmatrix} 3.6 & 1.8 \\\\ 0 & 1.1 \\end{bmatrix}"
        r_matrix = MathTex(r_matrix_template, color=r_color).scale(1).to_edge(LEFT, buff=0.5)
        
        # Create a version where we can highlight the zero
        r_matrix_highlight = MathTex(
            "R = \\begin{bmatrix} 3.6 & 1.8 \\\\ {0} & 1.1 \\end{bmatrix}"
        ).scale(1).to_edge(LEFT, buff=0.5)
        r_matrix_highlight[0][9].set_color(YELLOW)  # Highlight the zero
        
        # Create a shape highlighting the upper triangular structure
        triangle_shape = Polygon(
            r_matrix_highlight.get_corner(UL) + DOWN * 0.1 + RIGHT * 0.3,
            r_matrix_highlight.get_corner(UR) + DOWN * 0.1 + LEFT * 0.3,
            r_matrix_highlight.get_corner(DR) + UP * 0.1 + LEFT * 0.3,
            color=YELLOW, fill_opacity=0.2
        )
        
        # Labels for R matrix
        r_label = Text("R: Upper Triangular Matrix", font_size=30, color=r_color)
        r_label.to_edge(DOWN, buff=0.75)
        
        r_property = Text("Zeros below diagonal", font_size=24).next_to(r_label, DOWN, buff=0.2)
        
        # Display R matrix and highlight its structure
        self.play(
            Write(r_matrix),
            run_time=1
        )
        
        self.play(
            Transform(r_matrix, r_matrix_highlight),
            run_time=0.5
        )
        
        self.play(
            Create(triangle_shape),
            FadeIn(r_label),
            run_time=0.5
        )
        
        self.play(
            FadeIn(r_property),
            run_time=0.5
        )
        
        self.wait(1)
        
        #####################################
        # Section 5: Composition demonstration (8-12s)
        #####################################
        
        # Clear previous elements
        self.play(
            FadeOut(r_matrix),
            FadeOut(triangle_shape),
            FadeOut(r_label),
            FadeOut(r_property),
            FadeOut(standard_basis),
            run_time=0.5
        )
        
        # Create title for composition section
        composition_title = Text("Decomposition in action: A = Q × R", font_size=32)
        composition_title.to_edge(UP, buff=0.5)
        
        # Move equation
        self.play(
            Transform(equation, composition_title),
            run_time=1
        )
        
        # Create a split layout
        # Left side: standard basis
        # Center: Q transformation
        # Right: Full A transformation
        
        # Adjust the grid to be smaller
        grid.scale(0.6)
        grid.to_edge(DOWN, buff=0.5)
        
        # Create three distinct regions
        left_grid = grid.copy().shift(LEFT * 3.5)
        center_grid = grid.copy()
        right_grid = grid.copy().shift(RIGHT * 3.5)
        
        # Labels for each step
        step1_label = Text("Step 1: Standard Basis", font_size=20).next_to(left_grid, UP)
        step2_label = Text("Step 2: Q Rotation", font_size=20, color=q_color).next_to(center_grid, UP)
        step3_label = Text("Step 3: R Scaling → A", font_size=20, color=r_color).next_to(right_grid, UP)
        
        # Create standard basis vectors for each grid
        e1_left = Arrow(left_grid.c2p(0, 0), left_grid.c2p(1, 0), color=WHITE, buff=0)
        e2_left = Arrow(left_grid.c2p(0, 0), left_grid.c2p(0, 1), color=WHITE, buff=0)
        basis_left = VGroup(e1_left, e2_left)
        
        # Q transformation vectors
        q1_center = Arrow(center_grid.c2p(0, 0), center_grid.c2p(0.83, 0.55), color=q_color, buff=0)
        q2_center = Arrow(center_grid.c2p(0, 0), center_grid.c2p(-0.55, 0.83), color=q_color, buff=0)
        basis_center = VGroup(q1_center, q2_center)
        
        # A transformation vectors (final result)
        a1_right = Arrow(right_grid.c2p(0, 0), right_grid.c2p(3, 2), color=a_color, buff=0)
        a2_right = Arrow(right_grid.c2p(0, 0), right_grid.c2p(1, 2), color=a_color, buff=0)
        basis_right = VGroup(a1_right, a2_right)
        
        # Display grids and labels
        self.play(
            Create(left_grid),
            Create(center_grid),
            Create(right_grid),
            FadeIn(step1_label),
            FadeIn(step2_label),
            FadeIn(step3_label),
            run_time=1
        )
        
        # Show standard basis in all grids initially
        self.play(Create(basis_left), run_time=0.5)

if __name__ == "__main__":
    scene = QRDecompositionScene()
    scene.render()
