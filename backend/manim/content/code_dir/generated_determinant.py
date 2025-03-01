from manim import *

class DeterminantGeometricInterpretation(Scene):
    def construct(self):
        # Define colors for matrix elements
        a_color = BLUE
        b_color = GREEN
        c_color = ORANGE
        d_color = PURPLE
        
        # Scene 1: The matrix and determinant formula
        # Educational purpose: Introduce the algebraic representation of a determinant
        matrix = MathTex(
            r"\begin{bmatrix} a & b \\ c & d \end{bmatrix}"
        ).scale(1.5)
        
        # Color the matrix elements
        matrix[0][2].set_color(a_color)  # 'a'
        matrix[0][4].set_color(b_color)  # 'b'
        matrix[0][6].set_color(c_color)  # 'c'
        matrix[0][8].set_color(d_color)  # 'd'
        
        # Show the matrix
        self.play(FadeIn(matrix), run_time=1.5)
        self.wait(0.5)
        
        # Determinant formula
        det_formula = MathTex(
            r"\det(A) = ", r"a", r"\cdot", r"d", r"-", r"b", r"\cdot", r"c"
        ).scale(1.2)
        
        # Color the formula elements to match matrix
        det_formula[1].set_color(a_color)  # 'a'
        det_formula[3].set_color(d_color)  # 'd'
        det_formula[5].set_color(b_color)  # 'b'
        det_formula[7].set_color(c_color)  # 'c'
        
        det_formula.next_to(matrix, DOWN, buff=0.5)
        
        # Show the determinant formula
        self.play(Write(det_formula), run_time=1.5)
        self.wait(1)
        
        # Scene 2: Transition to geometric interpretation
        # Educational purpose: Set up geometric view while keeping algebraic reference
        matrix_and_formula = VGroup(matrix, det_formula)
        matrix_and_formula_small = matrix_and_formula.copy().scale(0.6).to_corner(UL, buff=0.5)
        
        # Move the formula to the corner and create grid
        self.play(
            Transform(matrix_and_formula, matrix_and_formula_small),
            run_time=1.5
        )
        
        # Create coordinate system
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            axis_config={"include_tip": False}
        ).scale(0.8).shift(DOWN * 0.5)
        
        # Draw the grid
        self.play(Create(axes), run_time=1.5)
        
        # Create unit square at the origin
        unit_square = Square(side_length=1, color=BLUE_D, fill_opacity=0.2, stroke_width=2)
        unit_square.move_to(axes.c2p(0.5, 0.5, 0))  # Center of square at (0.5, 0.5)
        
        # Show the unit square
        self.play(Create(unit_square), run_time=1)
        square_label = Text("Unit Square", font_size=24).next_to(unit_square, DOWN, buff=0.2)
        self.play(FadeIn(square_label), run_time=0.5)
        self.wait(0.5)
        
        # Scene 3: Show the column vectors of the matrix
        # Educational purpose: Demonstrate how matrix columns define transformation
        # Define points for the vectors
        origin = axes.c2p(0, 0, 0)
        point_a_c = axes.c2p(2, 3, 0)  # (a,c) = (2,3) for illustration
        point_b_d = axes.c2p(1, 2, 0)  # (b,d) = (1,2) for illustration
        
        # Create vectors
        vector1 = Arrow(origin, point_a_c, color=a_color, buff=0, max_tip_length_to_length_ratio=0.15)
        vector2 = Arrow(origin, point_b_d, color=b_color, buff=0, max_tip_length_to_length_ratio=0.15)
        
        vector_label1 = MathTex(r"(a, c) = (2, 3)", font_size=24).next_to(point_a_c, RIGHT, buff=0.1)
        vector_label1[0][:1].set_color(a_color)
        vector_label1[0][3:4].set_color(c_color)
        
        vector_label2 = MathTex(r"(b, d) = (1, 2)", font_size=24).next_to(point_b_d, RIGHT, buff=0.1)
        vector_label2[0][:1].set_color(b_color)
        vector_label2[0][3:4].set_color(d_color)
        
        # Create explanatory text
        vectors_title = Text("Column vectors of the matrix", font_size=28)
        vectors_title.to_edge(UP).shift(DOWN * 0.1)
        
        # Show the vectors
        self.play(
            FadeOut(square_label),
            Create(vector1), 
            Create(vector2),
            run_time=1.5
        )
        self.play(
            FadeIn(vector_label1),
            FadeIn(vector_label2),
            Write(vectors_title),
            run_time=1
        )
        self.wait(1)
        
        # Scene 4: Transform the unit square into a parallelogram
        # Educational purpose: Visualize how the matrix transforms space
        # Define the transformed parallelogram (based on matrix transformation)
        point_1 = origin  # Origin stays fixed
        point_2 = point_a_c  # First corner moves to (a,c)
        point_3 = axes.c2p(1+2, 2+3, 0)  # Diagonal corner moves to (a+b, c+d)
        point_4 = point_b_d  # Second corner moves to (b,d)
        
        parallelogram = Polygon(
            point_1, point_2, point_3, point_4,
            color=BLUE_D, fill_opacity=0.1, stroke_width=2
        )
        
        transform_title = Text("Matrix transforms unit square to parallelogram", font_size=28)
        transform_title.to_edge(UP).shift(DOWN * 0.1)
        
        # Transform the square to parallelogram
        self.play(
            FadeOut(vectors_title),
            FadeIn(transform_title),
            run_time=0.8
        )
        
        # Animate the transformation
        self.play(
            Transform(unit_square, parallelogram),
            run_time=2
        )
        self.wait(1)
        
        # Scene 5: Show that the area equals the determinant
        # Educational purpose: Connect geometric interpretation to algebraic formula
        area_text = MathTex(
            r"\text{Area} = |", r"\det(A)", r"| = |", r"ad", r"-", r"bc", r"|"
        ).scale(1)
        
        area_text[1].set_color(YELLOW)
        area_text[3][0].set_color(a_color)
        area_text[3][1].set_color(d_color)
        area_text[5][0].set_color(b_color)
        area_text[5][1].set_color(c_color)
        
        area_text.next_to(transform_title, DOWN, buff=0.3)
        
        # Fill the parallelogram to emphasize area
        self.play(
            unit_square.animate.set_fill(opacity=0.4),
            run_time=1
        )
        
        # Show the area formula
        self.play(Write(area_text), run_time=1.5)
        self.wait(1)
        
        # Scene 6: Example 1 - Positive determinant
        # Educational purpose: Show a concrete example with a positive determinant
        example_title = Text("Example 1: Positive Determinant", font_size=28)
        example_title.to_edge(UP).shift(DOWN * 0.1)
        
        example_matrix = MathTex(
            r"\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}"
        ).scale(1.2)
        
        example_det = MathTex(r"\det = 2 \cdot 3 - 0 \cdot 0 = 6").scale(1)
        example_group = VGroup(example_matrix, example_det).arrange(DOWN, buff=0.3)
        example_group.to_edge(LEFT).shift(RIGHT * 3 + UP * 0.5)
        
        # Create example rectangle (transformed square)
        example_rect = Rectangle(
            width=2, height=3, 
            color=GREEN_D, 
            fill_opacity=0.4,
            stroke_width=2
        )
        example_rect.move_to(axes.c2p(1, 1.5, 0))
        
        # Show example 1
        self.play(
            FadeOut(transform_title),
            FadeOut(area_text),
            FadeOut(vector_label1),
            FadeOut(vector_label2),
            FadeOut(vector1),
            FadeOut(vector2),
            FadeIn(example_title),
            run_time=0.8
        )
        
        self.play(
            Transform(unit_square, example_rect),
            FadeIn(example_group),
            run_time=1.5
        )
        
        area_label = Text("Area = 6", font_size=24, color=GREEN_D)
        area_label.next_to(example_rect, DOWN, buff=0.3)
        self.play(FadeIn(area_label), run_time=0.8)
        self.wait(1)
        
        # Scene 7: Example 2 - Negative determinant
        # Educational purpose: Show orientation change with negative determinant
        example2_title = Text("Example 2: Negative Determinant", font_size=28)
        example2_title.to_edge(UP).shift(DOWN * 0.1)
        
        example2_matrix = MathTex(
            r"\begin{bmatrix} 0 & 2 \\ 2 & 0 \end{bmatrix}"
        ).scale(1.2)
        
        example2_det = MathTex(r"\det = 0 \cdot 0 - 2 \cdot 2 = -4").scale(1)
        example2_group = VGroup(example2_matrix, example2_det).arrange(DOWN, buff=0.3)
        example2_group.to_edge(LEFT).shift(RIGHT * 3 + UP * 0.5)
        
        # Create example parallelogram with flipped orientation
        point_e1 = axes.c2p(0, 0, 0)
        point_e2 = axes.c2p(0, 2, 0)
        point_e3 = axes.c2p(2, 2, 0)
        point_e4 = axes.c2p(2, 0, 0)
        
        example2_shape = Polygon(
            point_e1, point_e2, point_e3, point_e4,
            color=RED_D,
            fill_opacity=0.4,
            stroke_width=2
        )
        
        # Show example 2
        self.play(
            FadeOut(example_title),
            FadeOut(example_group),
            FadeOut(area_label),
            FadeIn(example2_title),
            run_time=0.8
        )
        
        self.play(
            Transform(unit_square, example2_shape),
            FadeIn(example2_group),
            run_time=1.5
        )
        
        orientation_label = Text("Orientation flipped", font_size=24, color=RED_D)
        area_label2 = Text("Area = 4, Determinant = -4", font_size=24, color=RED_D)
        orientation_group = VGroup(orientation_label, area_label2).arrange(DOWN, buff=0.2)
        orientation_group.next_to(example2_shape, DOWN, buff=0.3)
        
        self.play(FadeIn(orientation_group), run_time=0.8)
        self.wait(1)
        
        # Scene 8: Final summary
        # Educational purpose: Consolidate learning with a memorable takeaway
        final_title = Text("Determinant: The scaling factor of area under transformation", 
                          font_size=32)
        final_title.to_edge(UP).shift(DOWN * 0.5)
        
        # Create a clean parallelogram for the final view
        final_parallelogram = Polygon(
            point_1, point_2, point_3, point_4,
            color=BLUE_D, fill_opacity=0.5, stroke_width=3
        )
        
        # Final transformation and message
        self.play(
            FadeOut(example2_title),
            FadeOut(example2_group),
            FadeOut(orientation_group),
            FadeOut(axes),
            FadeOut(matrix_and_formula),
            FadeIn(final_title),
            Transform(unit_square, final_parallelogram),
            run_time=1.5
        )
        
        # Add a caption about sign indicating orientation
        orientation_note = Text("Sign indicates orientation: + preserves, - reverses", 
                              font_size=24)
        orientation_note.next_to(final_title, DOWN, buff=0.5)
        
        self.play(FadeIn(orientation_note), run_time=0.8)
        self.wait(2)

if __name__ == "__main__":
    scene = DeterminantGeometricInterpretation()
    scene.render()