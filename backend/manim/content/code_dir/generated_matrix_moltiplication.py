from manim import *

class MatrixMultiplicationAnimation(Scene):
    def construct(self):
        # Set up colors for the matrices
        a_color = "#3498db"  # blue
        b_color = "#2ecc71"  # green
        c_color = "#9b59b6"  # purple
        highlight_color = "#f1c40f"  # golden yellow

        # -------- Create the matrices --------
        # Define the matrices with some simple values
        matrix_a_values = [[1, 2, 3], [4, 5, 6]]
        matrix_b_values = [[7, 8], [9, 10], [11, 12]]
        
        # Create matrix A (2×3)
        matrix_a = Matrix(
            matrix_a_values,
            h_buff=1.0,
            v_buff=0.8,
            bracket_h_buff=0.1,
            bracket_v_buff=0.1,
            element_to_mobject_config={"color": a_color}
        ).scale(0.7)
        
        # Create matrix B (3×2)
        matrix_b = Matrix(
            matrix_b_values,
            h_buff=1.0,
            v_buff=0.8,
            bracket_h_buff=0.1,
            bracket_v_buff=0.1,
            element_to_mobject_config={"color": b_color}
        ).scale(0.7)
        
        # Create empty result matrix C (2×2)
        matrix_c = Matrix(
            [[0, 0], [0, 0]],
            h_buff=1.0,
            v_buff=0.8,
            bracket_h_buff=0.1,
            bracket_v_buff=0.1,
            element_to_mobject_config={"color": c_color}
        ).scale(0.7)
        
        # Position the matrices
        matrix_a.move_to(LEFT * 3.5)
        matrix_b.move_to(RIGHT * 3.5)
        matrix_c.move_to(DOWN * 2.5)

        # -------- Matrix labels and dimensions --------
        # Create dimension labels
        a_dim_label = Tex("Matrix A (2×3)", color=a_color).next_to(matrix_a, UP)
        b_dim_label = Tex("Matrix B (3×2)", color=b_color).next_to(matrix_b, UP)
        c_dim_label = Tex("Result Matrix C (2×2)", color=c_color).next_to(matrix_c, UP)
        
        # 0-3s: Introduce matrices and check compatibility
        self.play(
            FadeIn(a_dim_label),
            Write(matrix_a),
            run_time=1.5
        )
        self.play(
            FadeIn(b_dim_label),
            Write(matrix_b),
            run_time=1.5
        )
        
        # Highlight the compatible dimensions (3 columns in A, 3 rows in B)
        inner_dim_a = SurroundingRectangle(VGroup(*[matrix_a.get_columns()[i] for i in range(3)]), color=highlight_color)
        inner_dim_b = SurroundingRectangle(VGroup(*[matrix_b.get_rows()[i] for i in range(3)]), color=highlight_color)
        
        compatibility_check = Tex("✓ Compatible dimensions", color=highlight_color).next_to(
            VGroup(matrix_a, matrix_b).get_center_of_mass(), DOWN * 0.8
        )
        
        self.play(
            Create(inner_dim_a),
            Create(inner_dim_b),
            run_time=1
        )
        self.play(Write(compatibility_check), run_time=1)
        self.wait(1)
        
        # 3-6s: Show resulting dimensions and create empty matrix C
        self.play(
            FadeOut(inner_dim_a),
            FadeOut(inner_dim_b),
            FadeOut(compatibility_check),
            run_time=0.5
        )
        
        # Show how result dimensions come from outer dimensions of A and B
        a_row_highlight = SurroundingRectangle(VGroup(*[matrix_a.get_rows()[i] for i in range(2)]), color=c_color)
        b_col_highlight = SurroundingRectangle(VGroup(*[matrix_b.get_columns()[i] for i in range(2)]), color=c_color)
        
        # Create arrows showing dimension mapping
        arrow_a_to_c = Arrow(
            start=a_row_highlight.get_left(),
            end=matrix_c.get_top() + LEFT * 0.5,
            color=c_color
        )
        
        arrow_b_to_c = Arrow(
            start=b_col_highlight.get_right(),
            end=matrix_c.get_top() + RIGHT * 0.5,
            color=c_color
        )
        
        dimension_text = Tex("Dimensions of C: (rows of A) × (columns of B) = 2 × 2", color=c_color).scale(0.8)
        dimension_text.next_to(matrix_c, DOWN)
        
        self.play(
            Create(a_row_highlight),
            Create(b_col_highlight),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            FadeIn(c_dim_label),
            GrowArrow(arrow_a_to_c),
            GrowArrow(arrow_b_to_c),
            run_time=1
        )
        
        self.play(
            Write(matrix_c),
            Write(dimension_text),
            run_time=1
        )
        self.wait(1)
        
        # Clean up for next phase
        self.play(
            FadeOut(a_row_highlight),
            FadeOut(b_col_highlight),
            FadeOut(arrow_a_to_c),
            FadeOut(arrow_b_to_c),
            FadeOut(dimension_text),
            run_time=0.5
        )
        
        # 6-9s: Calculate the first element (c₁₁)
        # Move matrices for better calculation view
        self.play(
            matrix_a.animate.scale(0.9).move_to(LEFT * 4 + UP * 1),
            matrix_b.animate.scale(0.9).move_to(RIGHT * 4 + UP * 1),
            matrix_c.animate.move_to(DOWN * 2),
            a_dim_label.animate.next_to(matrix_a, UP),
            b_dim_label.animate.next_to(matrix_b, UP),
            c_dim_label.animate.next_to(matrix_c, UP),
            run_time=1
        )
        
        # Highlight first row of A and first column of B
        row_a1 = SurroundingRectangle(matrix_a.get_rows()[0], color=a_color, buff=0.1)
        col_b1 = SurroundingRectangle(matrix_b.get_columns()[0], color=b_color, buff=0.1)
        
        self.play(
            Create(row_a1),
            Create(col_b1),
            run_time=0.8
        )
        
        # Set up calculation for c₁₁
        calc_position = UP * 0.5
        calc_scale = 0.8
        
        # Extract individual elements for animation
        a11 = matrix_a_values[0][0]
        a12 = matrix_a_values[0][1]
        a13 = matrix_a_values[0][2]
        b11 = matrix_b_values[0][0]
        b21 = matrix_b_values[1][0]
        b31 = matrix_b_values[2][0]
        
        # Create calculation display
        calc_step1 = MathTex(f"c_{{11}} = {a11} \\times {b11}", color=WHITE).scale(calc_scale).move_to(calc_position)
        calc_step2 = MathTex(f"c_{{11}} = {a11} \\times {b11} + {a12} \\times {b21}", color=WHITE).scale(calc_scale).move_to(calc_position)
        calc_step3 = MathTex(f"c_{{11}} = {a11} \\times {b11} + {a12} \\times {b21} + {a13} \\times {b31}", color=WHITE).scale(calc_scale).move_to(calc_position)
        calc_result = MathTex(f"c_{{11}} = {a11*b11 + a12*b21 + a13*b31}", color=c_color).scale(calc_scale).move_to(calc_position)
        
        # Element highlights
        a11_highlight = Indicate(matrix_a.get_entries()[0], color=highlight_color, scale_factor=1.5)
        b11_highlight = Indicate(matrix_b.get_entries()[0], color=highlight_color, scale_factor=1.5)
        
        a12_highlight = Indicate(matrix_a.get_entries()[1], color=highlight_color, scale_factor=1.5)
        b21_highlight = Indicate(matrix_b.get_entries()[2], color=highlight_color, scale_factor=1.5)
        
        a13_highlight = Indicate(matrix_a.get_entries()[2], color=highlight_color, scale_factor=1.5)
        b31_highlight = Indicate(matrix_b.get_entries()[4], color=highlight_color, scale_factor=1.5)
        
        # Animate first pair multiplication
        self.play(a11_highlight, b11_highlight, run_time=0.7)
        self.play(Write(calc_step1), run_time=0.7)
        
        # Animate second pair multiplication
        self.play(a12_highlight, b21_highlight, run_time=0.7)
        self.play(ReplacementTransform(calc_step1, calc_step2), run_time=0.7)
        
        # Animate third pair multiplication
        self.play(a13_highlight, b31_highlight, run_time=0.7)
        self.play(ReplacementTransform(calc_step2, calc_step3), run_time=0.7)
        
        # Show final result
        self.play(ReplacementTransform(calc_step3, calc_result), run_time=0.7)
        
        # Update the result in matrix C
        c11_val = matrix_a_values[0][0] * matrix_b_values[0][0] + \
                 matrix_a_values[0][1] * matrix_b_values[1][0] + \
                 matrix_a_values[0][2] * matrix_b_values[2][0]
        
        c11_result = MathTex(str(c11_val), color=c_color).move_to(matrix_c.get_entries()[0].get_center())
        
        self.play(
            ReplacementTransform(calc_result.copy(), c11_result),
            run_time=0.8
        )
        
        # Clean up for next calculations
        self.play(
            FadeOut(row_a1),
            FadeOut(col_b1),
            FadeOut(calc_result),
            run_time=0.5
        )
        
        # 9-12s: Calculate remaining elements rapidly
        # Prepare values for remaining calculations
        c12_val = matrix_a_values[0][0] * matrix_b_values[0][1] + \
                 matrix_a_values[0][1] * matrix_b_values[1][1] + \
                 matrix_a_values[0][2] * matrix_b_values[2][1]
        
        c21_val = matrix_a_values[1][0] * matrix_b_values[0][0] + \
                 matrix_a_values[1][1] * matrix_b_values[1][0] + \
                 matrix_a_values[1][2] * matrix_b_values[2][0]
        
        c22_val = matrix_a_values[1][0] * matrix_b_values[0][1] + \
                 matrix_a_values[1][1] * matrix_b_values[1][1] + \
                 matrix_a_values[1][2] * matrix_b_values[2][1]
        
        # Create MathTex objects for each result
        c12_result = MathTex(str(c12_val), color=c_color).move_to(matrix_c.get_entries()[1].get_center())
        c21_result = MathTex(str(c21_val), color=c_color).move_to(matrix_c.get_entries()[2].get_center())
        c22_result = MathTex(str(c22_val), color=c_color).move_to(matrix_c.get_entries()[3].get_center())
        
  