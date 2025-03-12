from manim import *
import numpy as np

class SVDVisualization(Scene):
    def construct(self):
        # ===== Setup the coordinate system and initial square =====
        # Create a 2D coordinate system for our transformations
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GRAY, "include_tip": True},
        )
        axes.set_z_index(0)
        
        # Create the initial blue square centered at origin
        square = Square(side_length=2, color=BLUE)
        square.set_fill(BLUE, opacity=0.5)
        square.set_z_index(1)
        
        # Define our transformation matrix A
        matrix_A = np.array([[3, 1], [1, 2]])
        
        # Calculate SVD components for later use
        U, sigma, Vt = np.linalg.svd(matrix_A)
        sigma_diag = np.diag(sigma)
        
        # ===== Start Animation (0-2s): Introduce square and matrix A =====
        self.play(Create(axes), run_time=1)
        self.play(Create(square), run_time=1)
        
        # Display the matrix A
        matrix_tex = MathTex(r"A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}")
        matrix_tex.to_edge(UP, buff=1)
        self.play(Write(matrix_tex), run_time=1)
        self.wait(0.5)
        
        # ===== Matrix Transformation (2-4s): Apply matrix A to transform square =====
        # Create the transformed shape by applying matrix A to the square
        transformed_square = square.copy()
        transformed_square.set_color(ORANGE)
        transformed_square.set_fill(ORANGE, opacity=0.5)
        transformed_square.apply_matrix(matrix_A)
        transformed_square.set_z_index(1)
        
        # Animate the transformation
        self.play(
            Transform(square, transformed_square),
            run_time=2
        )
        self.wait(0.5)
        
        # Add explanatory text
        transform_text = Text("Matrices transform shapes.", font_size=32)
        transform_text.to_edge(DOWN, buff=1)
        self.play(Write(transform_text), run_time=1)
        self.wait(1)
        
        # ===== Introducing SVD (4-6s): Revert to original square and show SVD equation =====
        # Revert back to the original square
        original_square = Square(side_length=2, color=BLUE)
        original_square.set_fill(BLUE, opacity=0.5)
        original_square.set_z_index(1)
        
        # Show the SVD equation
        svd_equation = MathTex(r"A = U \Sigma V^T")
        svd_equation.to_edge(UP, buff=1)
        
        # Label for original data
        original_label = Text("Original Data", font_size=24)
        original_label.next_to(original_square, DOWN, buff=0.5)
        
        # Animate the transition
        self.play(
            Transform(square, original_square),
            FadeOut(transform_text),
            ReplacementTransform(matrix_tex, svd_equation),
            FadeIn(original_label),
            run_time=2
        )
        self.wait(0.5)
        
        # ===== SVD Components Breakdown (6-11s): Show three sequential transformations =====
        # Original square for all transformations
        working_square = square.copy()
        
        # 1. V^T rotation transformation (first step of SVD)
        v_transform_text = MathTex(r"V^T", color=GREEN)
        v_transform_text.next_to(axes, UP, buff=0.5)
        v_transform_text.shift(LEFT * 3)
        
        # Apply V^T transformation
        rotated_square = working_square.copy()
        rotated_square.set_color(GREEN)
        rotated_square.set_fill(GREEN, opacity=0.5)
        rotated_square.apply_matrix(Vt)
        rotated_square.set_z_index(1)
        
        self.play(
            FadeIn(v_transform_text),
            run_time=0.5
        )
        self.play(
            Transform(working_square, rotated_square),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 2. Σ scaling transformation (second step of SVD)
        sigma_transform_text = MathTex(r"\Sigma", color=RED)
        sigma_transform_text.next_to(axes, UP, buff=0.5)
        
        # Apply Σ transformation (scaling)
        scaled_square = working_square.copy()
        scaled_square.set_color(RED)
        scaled_square.set_fill(RED, opacity=0.5)
        scaled_square.apply_matrix(sigma_diag)
        scaled_square.set_z_index(1)
        
        self.play(
            FadeIn(sigma_transform_text),
            run_time=0.5
        )
        self.play(
            Transform(working_square, scaled_square),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 3. U rotation transformation (third step of SVD)
        u_transform_text = MathTex(r"U", color=PURPLE)
        u_transform_text.next_to(axes, UP, buff=0.5)
        u_transform_text.shift(RIGHT * 3)
        
        # Apply U transformation (final rotation)
        final_square = working_square.copy()
        final_square.set_color(PURPLE)
        final_square.set_fill(PURPLE, opacity=0.5)
        final_square.apply_matrix(U)
        final_square.set_z_index(1)
        
        self.play(
            FadeIn(u_transform_text),
            run_time=0.5
        )
        self.play(
            Transform(working_square, final_square),
            run_time=1.5
        )
        self.wait(1)
        
        # Show that it matches the original transformation
        verification_text = Text("Same result as matrix A!", font_size=24, color=YELLOW)
        verification_text.to_edge(DOWN, buff=1)
        self.play(
            FadeIn(verification_text),
            run_time=1
        )
        self.wait(1)
        
        # ===== Final Sequence (11-15s): Combine all transformations with arrows =====
        # Clear the previous elements but keep coordinate system
        self.play(
            FadeOut(working_square),
            FadeOut(square),
            FadeOut(v_transform_text),
            FadeOut(sigma_transform_text),
            FadeOut(u_transform_text),
            FadeOut(original_label),
            FadeOut(verification_text),
            run_time=1
        )
        
        # Position for step-by-step sequence
        step_square1 = Square(side_length=1.5, color=BLUE)
        step_square1.set_fill(BLUE, opacity=0.5)
        step_square1.shift(LEFT * 4.5)
        step_square1.set_z_index(1)
        
        # V^T rotation
        step_square2 = step_square1.copy()
        step_square2.set_color(GREEN)
        step_square2.set_fill(GREEN, opacity=0.5)
        step_square2.apply_matrix(Vt)
        step_square2.shift(RIGHT * 3)
        step_square2.set_z_index(1)
        
        # Σ scaling
        step_square3 = step_square2.copy()
        step_square3.set_color(RED)
        step_square3.set_fill(RED, opacity=0.5)
        step_square3.apply_matrix(sigma_diag)
        step_square3.shift(RIGHT * 3)
        step_square3.set_z_index(1)
        
        # U rotation (final)
        step_square4 = step_square3.copy()
        step_square4.set_color(ORANGE)
        step_square4.set_fill(ORANGE, opacity=0.5)
        step_square4.apply_matrix(U)
        step_square4.shift(RIGHT * 3)
        step_square4.set_z_index(1)
        
        # Labels for each step
        label1 = Text("Original", font_size=20)
        label1.next_to(step_square1, DOWN, buff=0.5)
        
        label2 = Text("After V^T", font_size=20)
        label2.next_to(step_square2, DOWN, buff=0.5)
        
        label3 = Text("After Σ", font_size=20)
        label3.next_to(step_square3, DOWN, buff=0.5)
        
        label4 = Text("After U", font_size=20)
        label4.next_to(step_square4, DOWN, buff=0.5)
        
        # Create connecting arrows
        arrow1 = Arrow(step_square1.get_right(), step_square2.get_left(), color=WHITE)
        arrow1.set_z_index(0)
        
        arrow2 = Arrow(step_square2.get_right(), step_square3.get_left(), color=WHITE)
        arrow2.set_z_index(0)
        
        arrow3 = Arrow(step_square3.get_right(), step_square4.get_left(), color=WHITE)
        arrow3.set_z_index(0)
        
        # Step labels on arrows
        arrow_label1 = MathTex(r"V^T", color=GREEN, font_size=24)
        arrow_label1.next_to(arrow1, UP, buff=0.2)
        
        arrow_label2 = MathTex(r"\Sigma", color=RED, font_size=24)
        arrow_label2.next_to(arrow2, UP, buff=0.2)
        
        arrow_label3 = MathTex(r"U", color=PURPLE, font_size=24)
        arrow_label3.next_to(arrow3, UP, buff=0.2)
        
        # Animate the sequence
        self.play(
            FadeOut(axes),
            run_time=0.5
        )
        
        # Create highlighted SVD equation at bottom
        final_equation = MathTex(r"A = U \Sigma V^T")
        final_equation.scale(1.5)
        final_equation.to_edge(DOWN, buff=1.5)
        
        # Add a rectangular highlight behind the equation
        highlight_rect = SurroundingRectangle(final_equation, color=YELLOW, buff=0.2)
        highlight_rect.set_fill(YELLOW, opacity=0.15)
        highlight_rect.set_z_index(-1)
        
        # Create the tagline
        tagline = Text("SVD: Breaking down complex transformations into simple steps.", 
                      font_size=24)
        tagline.next_to(final_equation, DOWN, buff=0.5)
        
        # Show all elements sequentially
        self.play(
            FadeIn(step_square1),
            FadeIn(label1),
            run_time=0.5
        )
        
        self.play(
            Create(arrow1),
            FadeIn(arrow_label1),
            run_time=0.5
        )
        
        self.play(
            FadeIn(step_square2),
            FadeIn(label2),
            run_time=0.5
        )
        
        self.play(
            Create(arrow2),
            FadeIn(arrow_label2),
            run_time=0.5
        )
        
        self.play(
            FadeIn(step_square3),
            FadeIn(label3),
            run_time=0.5
        )
        
        self.play(
            Create(arrow3),
            FadeIn(arrow_label3),
            run_time=0.5
        )
        
        self.play(
            FadeIn(step_square4),
            FadeIn(label4),
            run_time=0.5
        )
        
        # Add the final equation and tagline
        self.play(
            FadeIn(highlight_rect),
            Write(final_equation),
            run_time=1
        )
        
        self.play(
            Write(tagline),
            run_time=1
        )
        
        # Give viewers time to absorb the complete visualization
        self.wait(2)

if __name__ == "__main__":
    scene = SVDVisualization()
    scene.render()