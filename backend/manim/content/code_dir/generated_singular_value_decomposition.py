from manim import *
import numpy as np

class SVDAnimation(Scene):
    def construct(self):
        # Define color scheme for SVD components
        v_color = BLUE_C
        sigma_color = GREEN_C
        u_color = RED_C
        
        #####################################
        # Section 1: Introduction (0-2s)
        #####################################
        
        # Create grid for reference
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        # Create a colorful square as our "image"
        square = Square(side_length=2)
        square.set_fill(opacity=0.8)
        square.set_sheen_direction(UL)
        square.set_fill(color=[BLUE, GREEN, YELLOW, RED])
        square.set_stroke(WHITE, width=3)
        
        # Add title and subtitle
        title = Text("Singular Value Decomposition", font_size=48)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text("Breaking complicated transformations into simple steps", 
                        font_size=32)
        subtitle.next_to(title, DOWN)
        
        # Display grid and square
        self.play(
            Create(grid, run_time=1),
            FadeIn(square, run_time=1)
        )
        self.wait(0.5)
        
        # Display title and subtitle
        self.play(
            Write(title, run_time=1),
            FadeIn(subtitle, run_time=1)
        )
        self.wait(0.5)
        
        #####################################
        # Section 2: Complex transformation (2-4s)
        #####################################
        
        # Define a transformation matrix
        transformation_matrix = np.array([
            [1.5, -0.7],
            [0.5, 1.2]
        ])
        
        # Create a label explaining the transformation
        transform_label = Text("Matrix A transforms our image in a complicated way", 
                              font_size=32)
        transform_label.to_edge(DOWN, buff=0.5)
        
        # Remove the title and subtitle, show the transformation label
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeIn(transform_label)
        )
        
        # Apply the complex transformation
        self.play(
            ApplyMatrix(transformation_matrix, square, run_time=2)
        )
        self.wait(0.5)
        
        # Store the transformed square for reference
        transformed_square = square.copy()
        
        #####################################
        # Section 3: Breaking down SVD (4-7s)
        #####################################
        
        # Reset the square to original state
        self.play(
            FadeOut(transform_label),
            ReplacementTransform(square, Square(side_length=2).set_fill(opacity=0.8)
                               .set_sheen_direction(UL)
                               .set_fill(color=[BLUE, GREEN, YELLOW, RED])
                               .set_stroke(WHITE, width=3))
        )
        square = Square(side_length=2).set_fill(opacity=0.8).set_sheen_direction(UL).set_fill(color=[BLUE, GREEN, YELLOW, RED]).set_stroke(WHITE, width=3)
        
        # Create three panels for the SVD breakdown
        self.play(
            square.animate.scale(0.6).move_to(LEFT * 4),
            FadeOut(grid)
        )
        
        # Create panel titles
        panel1_title = Text("Step 1: Rotation (V^T)", font_size=28, color=v_color)
        panel1_title.next_to(square, UP, buff=0.5)
        
        # First transformation: Rotation (V^T)
        # SVD concept: First, we rotate the square according to V^T
        self.play(
            FadeIn(panel1_title)
        )
        
        # Define the V^T rotation matrix (rotation by about 30 degrees)
        theta1 = np.pi/6
        v_t_matrix = np.array([
            [np.cos(theta1), -np.sin(theta1)],
            [np.sin(theta1), np.cos(theta1)]
        ])
        
        # Create the rotated square in the first panel
        rotated_square = square.copy()
        
        # Highlight the rotation with blue color
        self.play(
            rotated_square.animate.set_stroke(v_color, width=5),
            run_time=0.5
        )
        
        # Apply the V^T rotation
        self.play(
            Rotate(rotated_square, theta1, run_time=1.5)
        )
        self.wait(0.5)
        
        # Second panel: Scaling (Σ)
        rotated_square2 = rotated_square.copy()
        self.play(
            rotated_square2.animate.move_to(ORIGIN)
        )
        
        panel2_title = Text("Step 2: Scaling (Σ)", font_size=28, color=sigma_color)
        panel2_title.next_to(rotated_square2, UP, buff=0.5)
        
        self.play(
            FadeIn(panel2_title)
        )
        
        # Define the scaling factors
        scale_x = 1.5
        scale_y = 0.8
        
        # Highlight scaling with green color
        self.play(
            rotated_square2.animate.set_stroke(sigma_color, width=5),
            run_time=0.5
        )
        
        # Apply the Σ scaling
        self.play(
            rotated_square2.animate.stretch(scale_x, 0).stretch(scale_y, 1),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Third panel: Final rotation (U)
        scaled_square = rotated_square2.copy()
        self.play(
            scaled_square.animate.move_to(RIGHT * 4)
        )
        
        panel3_title = Text("Step 3: Final rotation (U)", font_size=28, color=u_color)
        panel3_title.next_to(scaled_square, UP, buff=0.5)
        
        self.play(
            FadeIn(panel3_title)
        )
        
        # Define the U rotation matrix (rotation by about 15 degrees)
        theta2 = np.pi/12
        u_matrix = np.array([
            [np.cos(theta2), -np.sin(theta2)],
            [np.sin(theta2), np.cos(theta2)]
        ])
        
        # Highlight the final rotation with red color
        self.play(
            scaled_square.animate.set_stroke(u_color, width=5),
            run_time=0.5
        )
        
        # Apply the U rotation
        self.play(
            Rotate(scaled_square, theta2, run_time=1.5)
        )
        self.wait(0.5)
        
        #####################################
        # Section 4: Combining transformations (7-11s)
        #####################################
        
        # Clear screen for the combined animation
        self.play(
            FadeOut(panel1_title),
            FadeOut(panel2_title),
            FadeOut(panel3_title),
            FadeOut(square),
            FadeOut(rotated_square),
            FadeOut(rotated_square2),
            FadeOut(scaled_square)
        )
        
        # Create new grid and original square
        new_grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        # Create fresh square for combined animation
        fresh_square = Square(side_length=2).set_fill(opacity=0.8).set_sheen_direction(UL).set_fill(color=[BLUE, GREEN, YELLOW, RED]).set_stroke(WHITE, width=3)
        
        self.play(
            Create(new_grid),
            FadeIn(fresh_square)
        )
        
        # Show title for the combined transformation
        combined_title = Text("Combining the three steps gives us our original transformation", 
                             font_size=32)
        combined_title.to_edge(UP, buff=0.5)
        
        self.play(
            Write(combined_title)
        )
        
        # Step 1: Apply V^T rotation (blue)
        step1_label = Text("Step 1: V^T (rotation)", font_size=28, color=v_color)
        step1_label.to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeIn(step1_label),
            fresh_square.animate.set_stroke(v_color, width=5)
        )
        
        self.play(
            Rotate(fresh_square, theta1, run_time=1)
        )
        self.wait(0.5)
        
        # Step 2: Apply Σ scaling (green)
        step2_label = Text("Step 2: Σ (scaling)", font_size=28, color=sigma_color)
        step2_label.to_edge(DOWN, buff=0.5)
        
        self.play(
            ReplacementTransform(step1_label, step2_label),
            fresh_square.animate.set_stroke(sigma_color, width=5)
        )
        
        self.play(
            fresh_square.animate.stretch(scale_x, 0).stretch(scale_y, 1),
            run_time=1
        )
        self.wait(0.5)
        
        # Step 3: Apply U rotation (red)
        step3_label = Text("Step 3: U (final rotation)", font_size=28, color=u_color)
        step3_label.to_edge(DOWN, buff=0.5)
        
        self.play(
            ReplacementTransform(step2_label, step3_label),
            fresh_square.animate.set_stroke(u_color, width=5)
        )
        
        self.play(
            Rotate(fresh_square, theta2, run_time=1)
        )
        self.wait(0.5)
        
        # Show the SVD equation
        self.play(
            FadeOut(step3_label)
        )
        
        eq_a = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=50)
        eq_a[0].set_color(WHITE)
        eq_a[2].set_color(u_color)  # U in red
        eq_a[3].set_color(sigma_color)  # Σ in green
        eq_a[4].set_color(v_color)  # V^T in blue
        
        eq_a.next_to(combined_title, DOWN, buff=0.5)
        
        self.play(
            Write(eq_a, run_time=1.5)
        )
        self.wait(1)
        
        #####################################
        # Section 5: Application example (11-15s)
        #####################################
        
        # Clear screen for the final example
        self.play(
            FadeOut(new_grid),
            FadeOut(fresh_square),
            FadeOut(combined_title)
        )
        
        # Create a photo placeholder (using a rectangle with image-like appearance)
        photo = Rectangle(height=3, width=4)
        photo.set_fill(color=BLUE_D, opacity=0.7)
        photo.set_stroke(WHITE, width=3)
        
        # Create a grid pattern inside to make it look like an image
        grid_lines = VGroup()
        for i in range(-10, 11):
            h_line = Line(
                start=[-2, i*0.15, 0],
                end=[2, i*0.15, 0],
                stroke_width=0.5,
                stroke_opacity=0.3
            )
            v_line = Line(
                start=[i*0.2, -1.5, 0],
                end=[i*0.2, 1.5, 0],
                stroke_width=0.5,
                stroke_opacity=0.3
            )
            grid_lines.add(h_line, v_line)
        
        # Add some colored shapes to make it look more image-like
        shapes = VGroup(
            Circle(radius=0.4).set_fill(RED, opacity=0.7).move_to([-1, 0.7, 0]),
            Triangle().scale(0.5).set_fill(GREEN, opacity=0.7).move_to([1, -0.5, 0]),
            Square().scale(0.3).set_fill(YELLOW, opacity=0.7).move_to([0.5, 0.8, 0])
        )
        
        photo_group = VGroup(photo, grid_lines, shapes)
        
        # Show the photo
        app_title = Text("SVD helps with image compression, data analysis, and more!", 
                         font_size=36)
        app_title.to_edge(UP, buff=0.5)
        
        self.play(
            FadeIn(photo_group),
            Write(app_title, run_time=1)
        )
        self.wait(0.5)
        
        # Show the photo decomposed into SVD components
        # Create smaller versions of transformations
        component1 = Square(side_length=1.2).set_stroke(v_color, width=4).set_fill(opacity=0.3)
        component1.move_to(LEFT * 3.5)
        
        component2 = Square(side_length=1.2).set_fill(opacity=0.3).set_stroke(sigma_color, width=4)
        component2.stretch(1.5, 0).stretch(0.7, 1)
        component2.move_to(ORIGIN)
        
        component3 = Square(side_length=1.2).set_fill(opacity=0.3).set_stroke(u_color, width=4)
        component3.stretch(1.5, 0).stretch(0.7, 1)
        component3.move_to(RIGHT * 3.5)
        
        # Create labels for components
        label1 = MathTex("V^T", font_size=40, color=v_color)
        label1.next_to(component1, DOWN, buff=0.3)
        
        label2 = MathTex("\\Sigma", font_size=40, color=sigma_color)
        label2.next_to(component2, DOWN, buff=0.3)
        
        label3 = MathTex("U", font_size=40, color=u_color)
        label3.next_to(component3, DOWN, buff=0.3)
        
        # Transform the photo into components
        self.play(
            ReplacementTransform(photo_group, VGroup(component1, component2, component3)),
            FadeIn(label1),
            FadeIn(label2),
            FadeIn(label3)
        )
        self.wait(1)
        
        # Show final SVD equation centered
        final_eq = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=64)
        final_eq[0].set_color(WHITE)
        final_eq[2].set_color(u_color)  # U in red
        final_eq[3].set_color(sigma_color)  # Σ in green
        final_eq[4].set_color(v_color)  # V^T in blue
        
        final_eq.move_to(ORIGIN)
        
        # Fade everything to the final equation
        self.play(
            FadeOut(app_title),
            FadeOut(component1),
            FadeOut(component2),
            FadeOut(component3),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(label3),
            FadeIn(final_eq, scale=1.2),
            run_time=1.5
        )
        
        # Add a concluding text
        conclusion = Text("Now you understand SVD!", font_size=36)
        conclusion.next_to(final_eq, DOWN, buff=0.8)
        
        self.play(
            Write(conclusion)
        )
        self.wait(1.5)

if __name__ == "__main__":
    scene = SVDAnimation()
    scene.render()