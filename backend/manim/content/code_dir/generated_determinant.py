from manim import *

class DeterminantAnimation(Scene):
    def construct(self):
        # Configure some constants for consistent positioning
        MATRIX_POSITION = RIGHT * 3.5
        FORMULA_POSITION = DOWN * 1.5 + RIGHT * 3.5
        
        # ---- SECTION 1: INTRODUCTION (0-2s) ----
        # Setup coordinate plane
        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 4, 1],
            axis_config={"include_numbers": True},
        ).scale(0.8)
        
        # Create the unit square
        unit_square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        unit_square.move_to(axes.c2p(0.5, 0.5, 0))
        
        # Label the vertices
        vertex_labels = VGroup()
        vertices = [(0, 0), (1, 0), (0, 1), (1, 1)]
        vertex_coords = []
        for v in vertices:
            coord = axes.c2p(v[0], v[1], 0)
            vertex_coords.append(coord)
            label = MathTex(f"({v[0]}, {v[1]})").scale(0.7)
            label.next_to(coord, DOWN + LEFT, buff=0.1)
            vertex_labels.add(label)
        
        # Create and display the title
        title = Text("Determinants", font_size=42)
        title.to_edge(UP, buff=0.2)
        
        # Add the elements to the scene
        self.play(
            Create(axes),
            FadeIn(unit_square),
            Write(title),
            run_time=2
        )
        self.play(FadeIn(vertex_labels), run_time=1)
        self.wait(0.5)
        
        # ---- SECTION 2: MATRIX INTRODUCTION (2-3s) ----
        # Display the matrix A
        matrix = MobjectMatrix(
            [
                [MathTex("2"), MathTex("1")],
                [MathTex("1"), MathTex("2")]
            ],
            left_bracket="[",
            right_bracket="]"
        )
        matrix.scale(0.9)
        matrix_label = MathTex("A = ").next_to(matrix, LEFT)
        matrix_group = VGroup(matrix_label, matrix).move_to(MATRIX_POSITION)
        
        self.play(
            FadeIn(matrix_group),
            run_time=1
        )
        self.wait(0.5)
        
        # ---- SECTION 3: TRANSFORMATION (3-6s) ----
        # Create the transformed parallelogram
        # Matrix A = [[2, 1], [1, 2]] transforms the vertices to:
        # (0,0) → (0,0), (1,0) → (2,1), (0,1) → (1,2), (1,1) → (3,3)
        transformed_vertices = [
            axes.c2p(0, 0, 0),
            axes.c2p(2, 1, 0),
            axes.c2p(1, 2, 0),
            axes.c2p(3, 3, 0)
        ]
        
        transformed_square = Polygon(
            *[transformed_vertices[i] for i in [0, 1, 3, 2]],  # Correct order for polygon
            color=GREEN,
            fill_opacity=0.5
        )
        
        # Create the movement paths and labels
        paths = VGroup()
        path_animations = []
        transformed_labels = VGroup()
        
        new_vertices = [(0, 0), (2, 1), (1, 2), (3, 3)]
        
        for i in range(4):
            # Create dotted path
            path = DashedLine(
                vertex_coords[i],
                transformed_vertices[i],
                dash_length=0.1,
                color=YELLOW
            )
            paths.add(path)
            
            # Create animation for following the path
            path_animations.append(
                MoveAlongPath(
                    vertex_labels[i].copy(), 
                    path
                )
            )
            
            # Create new labels
            new_label = MathTex(f"({new_vertices[i][0]}, {new_vertices[i][1]})").scale(0.7)
            new_label.next_to(transformed_vertices[i], UP + RIGHT, buff=0.1)
            transformed_labels.add(new_label)
        
        # Animation for the transformation
        self.play(
            Create(paths),
            run_time=1
        )
        
        self.play(
            Transform(unit_square, transformed_square),
            *path_animations,
            run_time=2
        )
        
        self.play(
            FadeOut(vertex_labels),
            FadeIn(transformed_labels),
            run_time=1
        )
        
        # Add the matrix multiplication explanation
        transform_label = MathTex(r"A \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x + 2y \end{bmatrix}")
        transform_label.scale(0.8).next_to(matrix_group, DOWN, buff=0.5)
        
        self.play(
            Write(transform_label),
            run_time=1
        )
        self.wait(0.5)
        
        # ---- SECTION 4: DETERMINANT CALCULATION (6-9s) ----
        # Show the determinant formula
        det_formula = MathTex(
            r"\det(A) = ad - bc"
        ).move_to(FORMULA_POSITION)
        
        self.play(
            Write(det_formula),
            run_time=1
        )
        
        # Substitute the values
        det_calc1 = MathTex(
            r"\det(A) = 2 \times 2 - 1 \times 1"
        ).move_to(FORMULA_POSITION)
        
        det_calc2 = MathTex(
            r"\det(A) = 4 - 1 = 3"
        ).move_to(FORMULA_POSITION)
        
        self.play(
            ReplacementTransform(det_formula, det_calc1),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            ReplacementTransform(det_calc1, det_calc2),
            run_time=1
        )
        self.wait(0.5)
        
        # Create a grid to visualize the area
        unit_grid = VGroup()
        
        # We want to fit exactly 3 unit squares to show area = 3
        # Calculate the grid lines based on the parallelogram
        for i in range(3):
            # Create a line for the diagonal division
            start_point = axes.c2p(i/3, 2*i/3, 0)
            end_point = axes.c2p(2 + i/3, 1 + 2*i/3, 0)
            diagonal = Line(start_point, end_point, stroke_width=2, color=WHITE)
            unit_grid.add(diagonal)
        
        # Add vertical lines for the grid
        for i in range(4):
            x_val = i * 2/3
            y_val = i * 1/3
            start = axes.c2p(x_val, y_val, 0)
            end = axes.c2p(x_val + 1, y_val + 2, 0)
            line = Line(start, end, stroke_width=2, color=WHITE)
            unit_grid.add(line)
        
        # Fill each unit area with a slightly different shade
        unit_squares = VGroup()
        colors = [GREEN_B, GREEN_C, GREEN_D]
        
        for i in range(3):
            unit_square_i = Polygon(
                axes.c2p(i*2/3, i*1/3, 0),
                axes.c2p(i*2/3 + 2/3, i*1/3 + 1/3, 0),
                axes.c2p(i*2/3 + 1/3, i*1/3 + 2/3, 0),
                axes.c2p(i*2/3, i*1/3, 0),
                color=colors[i],
                fill_opacity=0.3,
                stroke_width=0
            )
            unit_squares.add(unit_square_i)
        
        # Show the area grid animation
        self.play(
            Create(unit_grid),
            run_time=1
        )
        
        self.play(
            FadeIn(unit_squares),
            run_time=1
        )
        
        # Add a label showing the area
        area_label = Text("Area = 3", font_size=28)
        area_label.next_to(transformed_square, RIGHT, buff=0.5)
        
        self.play(
            Write(area_label),
            run_time=0.5
        )
        self.wait(1)
        
        # ---- SECTION 5: COMPARISON (9-12s) ----
        # Remove everything except the title
        self.play(
            FadeOut(unit_squares),
            FadeOut(unit_grid),
            FadeOut(paths),
            FadeOut(transform_label),
            FadeOut(transformed_labels),
            FadeOut(area_label),
            run_time=1
        )
        
        # Create side-by-side comparison
        # 1. Original unit square
        comparison_square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        original_area = Text("Area = 1", font_size=24)
        original_group = VGroup(comparison_square, original_area)
        original_area.next_to(comparison_square, DOWN, buff=0.2)
        
        # 2. Transformed parallelogram
        comparison_parallelogram = Polygon(
            *[transformed_vertices[i] for i in [0, 1, 3, 2]],
            color=GREEN,
            fill_opacity=0.5
        ).scale(0.5)
        transform_area = Text("Area = 3", font_size=24)
        transform_group = VGroup(comparison_parallelogram, transform_area)
        transform_area.next_to(comparison_parallelogram, DOWN, buff=0.2)
        
        # 3. Equation
        det_eq = MathTex(r"\det(A) = 3", font_size=36)
        
        # Position them in a row
        comparison = VGroup(original_group, transform_group, det_eq)
        comparison.arrange(RIGHT, buff=1.2)
        comparison.next_to(title, DOWN, buff=1)
        
        # Show the comparison
        self.play(
            FadeOut(axes),
            FadeOut(unit_square),
            FadeOut(transformed_square),
            FadeOut(matrix_group),
            FadeOut(det_calc2),
            run_time=1
        )
        
        self.play(
            FadeIn(comparison),
            run_time=1.5
        )
        
        # Arrow showing the transformation
        arrow = Arrow(
            original_group.get_right() + RIGHT * 0.1,
            transform_group.get_left() + LEFT * 0.1,
            buff=0.1,
            color=YELLOW
        )
        arrow_label = Text("× 3", font_size=24, color=YELLOW)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow),
            FadeIn(arrow_label),
            run_time=1
        )
        self.wait(1)
        
        # ---- SECTION 6: EXAMPLES (12-15s) ----
        # Remove the comparison
        self.play(
            FadeOut(comparison),
            FadeOut(arrow),
            FadeOut(arrow_label),
            run_time=1
        )
        
        # Create the summary title
        summary_title = Text("Determinant: The area scaling factor of a transformation", font_size=32)
        summary_title.to_edge(UP, buff=0.5)
        
        # Create the three examples
        example_scale = 0.7
        
        # Example 1: det = 0 (collapse to line)
        matrix1 = MathTex(r"A_1 = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}")
        square1 = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        
        # Collapsed square (line)
        collapsed_square = Line(
            LEFT * 0.5 + DOWN * 0.5,
            RIGHT * 0.5 + UP * 0.5,
            color=RED,
            stroke_width=4
        )
        
        ex1_det = MathTex(r"\det(A_1) = 0")
        ex1_caption = Text("Collapses to a line\n(non-invertible)", font_size=20)
        
        ex1_group = V