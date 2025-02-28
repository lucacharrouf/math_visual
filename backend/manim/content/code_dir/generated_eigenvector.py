from manim import *

class EigenvectorAnimation(Scene):
    def construct(self):
        # Set up the coordinate system with a light gray grid
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": LIGHT_GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # Create vectors that will be animated
        # Red vector (2,1) - regular vector
        red_vector = Arrow(
            ORIGIN, np.array([2, 1, 0]), 
            buff=0, 
            color=RED, 
            tip_length=0.2,
            stroke_width=4
        )
        red_vector_label = MathTex("\\vec{v}_1", color=RED).next_to(red_vector.get_end(), UP+RIGHT, buff=0.1)
        
        # Blue vector (1,2) - eigenvector
        blue_vector = Arrow(
            ORIGIN, np.array([1, 2, 0]), 
            buff=0, 
            color=BLUE, 
            tip_length=0.2,
            stroke_width=4
        )
        blue_vector_label = MathTex("\\vec{v}_2", color=BLUE).next_to(blue_vector.get_end(), UP+LEFT, buff=0.1)
        
        # Phase 1: Setting up the scene (0-3s)
        # Fade in the grid
        self.play(Create(plane), run_time=1)
        
        # First caption
        caption = Text("What happens during a transformation?", font_size=36)
        caption.to_edge(DOWN, buff=1)
        
        # Create the vectors
        self.play(
            Create(red_vector),
            Create(blue_vector),
            run_time=1
        )
        self.play(
            FadeIn(red_vector_label),
            FadeIn(blue_vector_label),
            FadeIn(caption),
            run_time=1
        )
        self.wait(1)
        
        # Phase 2: Applying the transformation (3-7s)
        # Store original positions for reference
        original_red_endpoint = red_vector.get_end()
        original_blue_endpoint = blue_vector.get_end()
        
        # Prepare dashed line for tracking original direction of red vector
        dashed_line = DashedLine(
            ORIGIN, original_red_endpoint, 
            color=RED_E, 
            dash_length=0.1,
            dashed_ratio=0.5,
            stroke_opacity=0.7
        )
        
        # Define the transformation matrix [2,1][0,1]
        matrix = [[2, 1], [0, 1]]
        matrix_tex = MathTex(
            "A = \\begin{bmatrix} 2 & 1 \\\\ 0 & 1 \\end{bmatrix}"
        ).scale(0.8).to_corner(UL, buff=0.5)
        
        # Fade out the caption and show transformation matrix
        self.play(
            FadeOut(caption),
            FadeIn(matrix_tex),
            run_time=1
        )
        
        # Apply the matrix transformation to the plane and vectors
        self.play(
            ApplyMatrix(matrix, plane),
            ApplyMatrix(matrix, red_vector),
            ApplyMatrix(matrix, blue_vector),
            ApplyMatrix(matrix, red_vector_label),
            ApplyMatrix(matrix, blue_vector_label),
            run_time=2
        )
        self.wait(0.5)
        
        # Show the original direction of the red vector with a dashed line
        self.play(
            Create(dashed_line),
            run_time=1
        )
        
        # Add text pointing out the direction change for red vector
        red_direction_text = Text("Direction changed", font_size=24, color=RED)
        red_direction_text.next_to(red_vector.get_end(), RIGHT, buff=0.3)
        self.play(FadeIn(red_direction_text), run_time=0.5)
        self.wait(1)
        
        # Phase 3: Explaining the eigenvector concept (7-9s)
        # Highlight that the blue vector is an eigenvector
        eigenvector_text = Text("The blue vector is an eigenvector", font_size=36)
        eigenvector_text.to_edge(DOWN, buff=1)
        
        self.play(
            FadeOut(red_direction_text),
            FadeIn(eigenvector_text),
            run_time=1
        )
        
        # Make the blue vector pulse to emphasize it
        self.play(
            Indicate(blue_vector, scale_factor=1.2, color=BLUE_A),
            run_time=1
        )
        
        # Add eigenvalue label
        eigenvalue_label = MathTex("\\lambda = 2", color=BLUE)
        eigenvalue_label.next_to(blue_vector.get_end(), UP, buff=0.3)
        
        # Show the eigenvalue
        self.play(
            FadeIn(eigenvalue_label),
            run_time=1
        )
        self.wait(0.5)
        
        # Phase 4: Show the mathematical equation (9-12s)
        # Instead of scaling the camera frame, scale the entire scene
        all_objects = Group(*self.mobjects)
        
        # Scale down slightly to make room for the equation
        self.play(
            all_objects.animate.scale(0.9).shift(DOWN*0.5),
            run_time=1
        )
        
        # Create the eigenvector equation
        eigenvector_eq = MathTex(
            "A\\vec{v} = \\lambda\\vec{v}",
            substrings_to_isolate=["A", "\\vec{v}", "=", "\\lambda", "\\vec{v}"]
        ).scale(1.2)
        eigenvector_eq.to_edge(UP, buff=0.5)
        
        # Animate the equation appearing
        self.play(
            FadeOut(eigenvector_text),
            FadeIn(eigenvector_eq),
            run_time=1
        )
        
        # Animate the equation to show A*v = λ*v
        # First, create the expanded equation
        expanded_eq_left = MathTex(
            "\\begin{bmatrix} 2 & 1 \\\\ 0 & 1 \\end{bmatrix}",
            "\\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}"
        ).scale(0.9)
        
        expanded_eq_right = MathTex(
            "2",
            "\\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}"
        ).scale(0.9)
        
        equals = MathTex("=").scale(0.9)
        
        expanded_group = VGroup(expanded_eq_left, equals, expanded_eq_right)
        expanded_group.arrange(RIGHT, buff=0.3)
        expanded_group.next_to(eigenvector_eq, DOWN, buff=0.5)
        
        # Show the expanded equation
        self.play(
            FadeIn(expanded_group),
            run_time=1
        )
        
        # Calculate the result of the matrix multiplication
        result_eq = MathTex(
            "\\begin{bmatrix} 2 \\cdot 1 + 1 \\cdot 2 \\\\ 0 \\cdot 1 + 1 \\cdot 2 \\end{bmatrix}",
            "=",
            "\\begin{bmatrix} 4 \\\\ 2 \\end{bmatrix}",
            "=",
            "2 \\cdot \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}"
        ).scale(0.8)
        result_eq.next_to(expanded_group, DOWN, buff=0.5)
        
        self.play(
            FadeIn(result_eq),
            run_time=1
        )
        self.wait(1)
        
        # Phase 5: Final summary (12-15s)
        # Clear some elements to reduce visual clutter
        self.play(
            FadeOut(expanded_group),
            FadeOut(result_eq),
            FadeOut(dashed_line),
            FadeOut(red_vector_label),
            FadeOut(matrix_tex),
            run_time=1
        )
        
        # Create final summary text
        final_text = Text("Same direction, scaled by λ = 2", font_size=32, color=BLUE)
        final_text.to_edge(DOWN, buff=1)
        
        # Add an arrow pointing to the eigenvector
        pointer = Arrow(
            final_text.get_top() + UP*0.2,
            blue_vector.get_center(),
            buff=0.3,
            color=YELLOW
        )
        
        # Show the final summary
        self.play(
            FadeIn(final_text),
            Create(pointer),
            run_time=1
        )
        
        # Final emphasis on the eigenvector equation
        self.play(
            Indicate(eigenvector_eq, scale_factor=1.1, color=YELLOW),
            run_time=1
        )
        
        # Emphasize the eigenvector one more time
        self.play(
            Indicate(blue_vector, scale_factor=1.2, color=BLUE_A),
            run_time=1
        )
        
        # Final pause to let the concept sink in
        self.wait(2)

if __name__ == "__main__":  # Fixed from "__init__" to "__main__"
    scene = EigenvectorAnimation()
    scene.render()