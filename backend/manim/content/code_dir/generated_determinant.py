from manim import *

class DeterminantVisualization(Scene):
    def construct(self):
        # Setting up constants for consistent use
        BLUE_VECTOR = "#3090FF"  # i vector color
        RED_VECTOR = "#FF3030"   # j vector color
        PURPLE_FILL = "#7030A0"  # unit square color
        GREEN_FILL = "#30A050"   # transformed area color
        
        # Create a coordinate system for our vectors
        axes = Axes(
            x_range=[-3, 6, 1],
            y_range=[-3, 6, 1],
            axis_config={"include_tip": False, "include_numbers": True},
        ).scale(0.8)
        
        # Add grid lines for better visualization
        grid = NumberPlane(
            x_range=[-3, 6, 1],
            y_range=[-3, 6, 1],
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(0.8)
        
        # Start with a clean coordinate plane
        self.play(
            Create(grid, run_time=1),
            Create(axes, run_time=1)
        )
        
        # Create and display the unit vectors
        i_vector = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1, 0), 
                        color=BLUE_VECTOR, buff=0, stroke_width=4)
        j_vector = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(0, 1), 
                        color=RED_VECTOR, buff=0, stroke_width=4)
        
        i_label = MathTex("\\vec{i}", color=BLUE_VECTOR).next_to(i_vector.get_end(), DOWN, buff=0.1)
        j_label = MathTex("\\vec{j}", color=RED_VECTOR).next_to(j_vector.get_end(), LEFT, buff=0.1)
        
        # Create unit square with light purple fill
        unit_square = Polygon(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 0),
            axes.coords_to_point(1, 1),
            axes.coords_to_point(0, 1),
            color=PURPLE_FILL,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        # Display unit vectors and unit square
        self.play(
            Create(i_vector, run_time=0.8),
            Create(j_vector, run_time=0.8),
            FadeIn(unit_square, run_time=0.8)
        )
        self.play(
            Write(i_label),
            Write(j_label)
        )
        self.wait(0.5)
        
        # Add labels for unit vectors values
        i_value = MathTex("[1, 0]", color=BLUE_VECTOR).next_to(i_vector.get_end(), DOWN, buff=0.25)
        j_value = MathTex("[0, 1]", color=RED_VECTOR).next_to(j_vector.get_end(), RIGHT, buff=0.25)
        
        self.play(
            Write(i_value),
            Write(j_value)
        )
        self.wait(0.5)
        
        # ----------- First matrix transformation (Matrix A) -----------
        # Display Matrix A in top right corner
        matrix_A = MathTex(
            "A = \\begin{bmatrix} 3 & 1 \\\\ 2 & 2 \\end{bmatrix}"
        ).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        matrix_A_label = Text("Matrix A", font_size=24).next_to(matrix_A, UP, buff=0.2)
        
        self.play(
            Write(matrix_A, run_time=1),
            Write(matrix_A_label, run_time=1)
        )
        self.wait(0.5)
        
        # Calculate the transformed vectors
        # i' = [3, 2], j' = [1, 2]
        transformed_i_vector = Arrow(
            axes.coords_to_point(0, 0), 
            axes.coords_to_point(3, 2), 
            color=BLUE_VECTOR, buff=0, stroke_width=4
        )
        transformed_j_vector = Arrow(
            axes.coords_to_point(0, 0), 
            axes.coords_to_point(1, 2), 
            color=RED_VECTOR, buff=0, stroke_width=4
        )
        
        # Create the trace paths for the transforming vectors
        i_path = DashedLine(
            i_vector.get_end(), 
            transformed_i_vector.get_end(), 
            color=BLUE_VECTOR, 
            stroke_opacity=0.5
        )
        j_path = DashedLine(
            j_vector.get_end(), 
            transformed_j_vector.get_end(), 
            color=RED_VECTOR, 
            stroke_opacity=0.5
        )
        
        # Transformation of vectors and square
        self.play(
            Create(i_path, run_time=0.5),
            Create(j_path, run_time=0.5)
        )
        
        # Update vector value labels
        transformed_i_value = MathTex("[3, 2]", color=BLUE_VECTOR).next_to(transformed_i_vector.get_end(), RIGHT, buff=0.25)
        transformed_j_value = MathTex("[1, 2]", color=RED_VECTOR).next_to(transformed_j_vector.get_end(), UP, buff=0.25)
        
        # Create the parallelogram after transformation
        transformed_square = Polygon(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(3, 2),
            axes.coords_to_point(4, 4),
            axes.coords_to_point(1, 2),
            color=GREEN_FILL,
            fill_opacity=0.0,  # Start with zero opacity, will animate it later
            stroke_width=0
        )
        
        # Animate the transformation
        self.play(
            ReplacementTransform(i_vector, transformed_i_vector, run_time=1.5),
            ReplacementTransform(j_vector, transformed_j_vector, run_time=1.5),
            ReplacementTransform(i_value, transformed_i_value, run_time=1.5),
            ReplacementTransform(j_value, transformed_j_value, run_time=1.5),
            ReplacementTransform(unit_square, transformed_square, run_time=1.5),
            ReplacementTransform(i_label, MathTex("A\\vec{i}", color=BLUE_VECTOR).next_to(transformed_i_vector.get_end(), RIGHT, buff=0.1), run_time=1.5),
            ReplacementTransform(j_label, MathTex("A\\vec{j}", color=RED_VECTOR).next_to(transformed_j_vector.get_end(), UP, buff=0.1), run_time=1.5),
        )
        self.wait(0.5)
        
        # Highlight the parallelogram and show its area
        self.play(
            transformed_square.animate.set_fill(opacity=0.4),
            run_time=1
        )
        
        area_text = MathTex("\\text{Area} = 4").next_to(transformed_square, DOWN, buff=0.5)
        area_text.shift(RIGHT * 1)  # Move it a bit to the right for better visibility
        
        self.play(Write(area_text))
        self.wait(0.5)
        
        # Show the determinant calculation
        det_calc = MathTex(
            "\\det(A)", "=", "3 \\times 2", "-", "1 \\times 2", "=", "6", "-", "2", "=", "4"
        ).next_to(matrix_A, DOWN, buff=0.5)
        
        # Animate the determinant calculation step by step
        self.play(Write(det_calc[0:2]), run_time=0.8)  # det(A) =
        self.play(Write(det_calc[2]), run_time=0.6)    # 3 × 2
        self.play(Write(det_calc[3:5]), run_time=0.6)  # - 1 × 2
        self.play(Write(det_calc[5:7]), run_time=0.6)  # = 6
        self.play(Write(det_calc[7:9]), run_time=0.6)  # - 2
        self.play(Write(det_calc[9:]), run_time=0.6)   # = 4
        
        # Highlight the final determinant result
        det_result_box = SurroundingRectangle(det_calc[-1], color=YELLOW)
        self.play(Create(det_result_box))
        
        # Connect the determinant to the area
        det_area_arrow = Arrow(
            det_calc[-1].get_bottom() + DOWN * 0.1,
            area_text.get_top() + UP * 0.1,
            color=YELLOW,
            buff=0.1
        )
        
        self.play(Create(det_area_arrow))
        self.wait(1)
        
        # ----------- Second matrix transformation (Matrix B) -----------
        # Cleanup previous elements
        self.play(
            FadeOut(area_text),
            FadeOut(det_area_arrow),
            FadeOut(det_result_box),
            FadeOut(det_calc),
            FadeOut(transformed_i_value),
            FadeOut(transformed_j_value),
            FadeOut(i_path),
            FadeOut(j_path),
            FadeOut(transformed_square),
            FadeOut(matrix_A_label),
            run_time=1
        )
        
        # Show Matrix B
        matrix_B = MathTex(
            "B = \\begin{bmatrix} 2 & 1 \\\\ -1 & 1 \\end{bmatrix}"
        ).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        matrix_B_label = Text("Matrix B", font_size=24).next_to(matrix_B, UP, buff=0.2)
        
        self.play(
            ReplacementTransform(matrix_A, matrix_B),
            Write(matrix_B_label)
        )
        self.wait(0.5)
        
        # Calculate new transformed vectors for matrix B
        # i' = [2, -1], j' = [1, 1]
        new_i_vector = Arrow(
            axes.coords_to_point(0, 0), 
            axes.coords_to_point(2, -1), 
            color=BLUE_VECTOR, buff=0, stroke_width=4
        )
        new_j_vector = Arrow(
            axes.coords_to_point(0, 0), 
            axes.coords_to_point(1, 1), 
            color=RED_VECTOR, buff=0, stroke_width=4
        )
        
        # Create trace paths for the vectors
        new_i_path = DashedLine(
            transformed_i_vector.get_end(), 
            new_i_vector.get_end(), 
            color=BLUE_VECTOR, 
            stroke_opacity=0.5
        )
        new_j_path = DashedLine(
            transformed_j_vector.get_end(), 
            new_j_vector.get_end(), 
            color=RED_VECTOR, 
            stroke_opacity=0.5
        )
        
        # Show the transformation paths
        self.play(
            Create(new_i_path, run_time=0.5),
            Create(new_j_path, run_time=0.5)
        )
        
        # New vector labels
        new_i_value = MathTex("[2, -1]", color=BLUE_VECTOR).next_to(new_i_vector.get_end(), DOWN, buff=0.25)
        new_j_value = MathTex("[1, 1]", color=RED_VECTOR).next_to(new_j_vector.get_end(), RIGHT, buff=0.25)
        
        # Create the new parallelogram (with reversed orientation)
        new_parallelogram = Polygon(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(2, -1),
            axes.coords_to_point(3, 0),
            axes.coords_to_point(1, 1),
            color=RED_A,
            fill_opacity=0.0,
            stroke_width=0
        )
        
        # Animate the transformation
        self.play(
            ReplacementTransform(transformed_i_vector, new_i_vector, run_time=1.5),
            ReplacementTransform(transformed_j_vector, new_j_vector, run_time=1.5),
            Write(new_i_value, run_time=1),
            Write(new_j_value, run_time=1),
            FadeIn(new_parallelogram, run_time=1.5)
        )
        self.wait(0.5)
        
        # Highlight the new parallelogram
        self.play(
            new_parallelogram.animate.set_fill(opacity=0.4),
            run_time=1
        )
        
        # Show that this parallelogram has reversed orientation
        orientation_text = Text("Reversed Orientation", font_size=24, color=RED).next_to(new_parallelogram, DOWN, buff=0.5)
        orientation_text.shift(RIGHT * 0.5)
        
        self.play(Write(orientation_text))
        
        # Show the determinant calculation for Matrix B
        det_calc_B = MathTex(
            "\\det(B)", "=", "2 \\times 1", "-", "1 \\times (-1)", "=", "2", "+", "1", "=", "3"
        ).next_to(matrix_B, DOWN, buff=0.5)
        
        # Add the negative sign to emphasize orientation reversal
        negative_sign = MathTex("-").next_to(det_calc_B, LEFT, buff=0.1).set_color(RED)
        
        # Animate calculation step by step
        self.play(Write(det_calc_B[0:2]), run_time=0.7)  # det(B) =
        self.play(Write(det_calc_B[2]), run_time=0.6)    # 2 × 1
        self.play(Write(det_calc_B[3:5]), run_time=0.6)  # - 1 × (-1)
        self.play(Write(det_calc_B[5:7]), run_time=0.6)  # = 2
        self.play(Write(det_calc_B[7:9]), run_time=0.6)  # + 1
        self.play(Write(det_calc_B[9:]), run_time=0.6)   # = 3
        
        # Add negative sign to show orientation reversal
        self.play(Write(negative_sign))
        
        # Highlight the negative determinant
        final_result = VGroup(negative_sign, det_calc_B[-1])
        neg_det_box = SurroundingRectangle(final_result, color=RED)
        
        self.play(Create(neg_det_box))
        
        # Add explanation text about negative determinant
        neg_det_text = Text("Negative determinant = Reversed orientation", 
                          font_size=22, color=RED).next_to(det_calc_B, DOWN, buff=0.5)
        
        self.play(Write(neg_det_text))
        self.wait(1)
        
        # ----------- Third matrix transformation (Matrix C - Singular) -----------
        # Cleanup previous elements
        self.play(
            FadeOut(neg_det_text),
            FadeOut(neg_det_box),
            FadeOut(det_calc_B),
            FadeOut(negative_sign),
            FadeOut(orientation_text),
            FadeOut(new_i_value),
            FadeOut(new_j_value),
            FadeOut(new_i_path),
            FadeOut(new_j_path),
            FadeOut(new_parallelogram),