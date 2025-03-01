from manim import *

class EigenvectorAnimation(Scene):
    def construct(self):
        # Set up the transformation matrix
        transformation_matrix = [[2, 0], [0, 3]]
        
        # Define colors for consistency
        square_color = "#2C7CB9"
        x_eigenvector_color = RED
        y_eigenvector_color = BLUE
        
        #############################
        # PART 1: Intro and Grid Transformation (0-3s)
        #############################
        
        # Create the coordinate system - fundamental for understanding linear transformations
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY, "include_numbers": True, "numbers_to_include": [-4, -2, 2, 4]}
        ).scale(0.8)
        
        # Add grid lines to help visualize the transformation effect on space
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(0.8)
        grid.set_opacity(0.3)
        
        # Create a square to demonstrate how shapes transform
        square = Square(side_length=2, color=square_color, fill_opacity=0.5).scale(0.8)
        
        # Introduce the coordinate system
        self.play(Create(axes), run_time=1.5)
        self.wait(0.5)
        
        # Add the grid and square to establish the initial state
        self.play(
            FadeIn(grid),
            FadeIn(square),
            run_time=1
        )
        self.wait(0.5)
        
        # Introduce the concept of linear transformation
        title = Text("Linear Transformation", font_size=36).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        
        # Apply the transformation to both grid and square to visualize effect
        self.play(
            ApplyMatrix(transformation_matrix, grid),
            ApplyMatrix(transformation_matrix, square),
            run_time=1.5
        )
        self.wait(0.5)
        
        #############################
        # PART 2: Introduce Eigenvectors (3-6s)
        #############################
        
        # Create eigenvectors (standard basis vectors in this case)
        eigenvector_x = Arrow(
            axes.c2p(0, 0), axes.c2p(2, 0), 
            color=x_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        eigenvector_y = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 2), 
            color=y_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        # Original vectors before transformation (thin versions for comparison)
        original_x = Arrow(
            axes.c2p(0, 0), axes.c2p(2, 0), 
            color=x_eigenvector_color, 
            buff=0, 
            stroke_width=2,
            stroke_opacity=0.5,
            max_tip_length_to_length_ratio=0.15
        )
        
        original_y = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 2), 
            color=y_eigenvector_color, 
            buff=0, 
            stroke_width=2,
            stroke_opacity=0.5,
            max_tip_length_to_length_ratio=0.15
        )
        
        # Introduce the eigenvectors
        self.play(
            Create(eigenvector_x),
            Create(eigenvector_y),
            run_time=1
        )
        self.wait(0.5)
        
        # Store the original vectors for comparison later
        self.add(original_x, original_y)
        self.remove(original_x, original_y)  # Don't show them yet
        
        # Apply transformation to eigenvectors to demonstrate their special property
        transformed_x = Arrow(
            axes.c2p(0, 0), axes.c2p(4, 0), 
            color=x_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        transformed_y = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 6), 
            color=y_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        # Show the transformation of the eigenvectors
        self.play(
            ReplacementTransform(eigenvector_x, transformed_x),
            ReplacementTransform(eigenvector_y, transformed_y),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Re-add the original vectors for comparison to show direction preservation
        self.play(
            FadeIn(original_x),
            FadeIn(original_y),
            run_time=0.8
        )
        self.wait(0.5)
        
        #############################
        # PART 3: Explain Eigenvectors (6-9s)
        #############################
        
        # Update title to focus on eigenvectors
        eigenvector_title = Text("Eigenvectors", font_size=36).to_edge(UP)
        
        # Create equation Av = λv
        equation = MathTex("A", "\\vec{v}", "=", "\\lambda", "\\vec{v}").scale(1.2).next_to(eigenvector_title, DOWN)
        
        # Arrows pointing to the eigenvectors for emphasis
        arrow_to_x = Arrow(
            start=axes.c2p(3, 0.5), 
            end=axes.c2p(3, 0), 
            color=x_eigenvector_color,
            buff=0.1
        )
        
        arrow_to_y = Arrow(
            start=axes.c2p(0.5, 3), 
            end=axes.c2p(0, 3), 
            color=y_eigenvector_color,
            buff=0.1
        )
        
        # Labels for the eigenvectors
        x_label = Text("Eigenvector 1", font_size=20, color=x_eigenvector_color).next_to(arrow_to_x, UP)
        y_label = Text("Eigenvector 2", font_size=20, color=y_eigenvector_color).next_to(arrow_to_y, RIGHT)
        
        # Transition the title and add the equation
        self.play(
            ReplacementTransform(title, eigenvector_title),
            run_time=0.8
        )
        self.play(Write(equation), run_time=1.2)
        self.wait(0.5)
        
        # Add labels and arrows pointing to eigenvectors
        self.play(
            Create(arrow_to_x),
            Create(arrow_to_y),
            run_time=0.8
        )
        self.play(
            Write(x_label),
            Write(y_label),
            run_time=1
        )
        self.wait(0.5)
        
        # Highlight how the vectors remain parallel to their originals
        parallel_text = Text("Notice: Direction preserved, only length changes", 
                            font_size=24).to_edge(DOWN, buff=0.5)
        self.play(Write(parallel_text), run_time=1)
        self.wait(0.5)
        
        #############################
        # PART 4: Emphasize Eigenvalues (9-12s)
        #############################
        
        # Fade out some elements to focus on eigenvalues
        self.play(
            FadeOut(parallel_text),
            FadeOut(arrow_to_x),
            FadeOut(arrow_to_y),
            FadeOut(x_label),
            FadeOut(y_label),
            run_time=0.8
        )
        
        # Create eigenvalue labels
        eigenvalue_title = Text("Eigenvalues", font_size=36).to_edge(UP)
        
        x_eigenvalue_label = MathTex("\\lambda_1 = 2", color=x_eigenvector_color).next_to(
            transformed_x.get_end(), UR, buff=0.5
        )
        
        y_eigenvalue_label = MathTex("\\lambda_2 = 3", color=y_eigenvector_color).next_to(
            transformed_y.get_end(), RIGHT, buff=0.5
        )
        
        # Update the title and show eigenvalues
        self.play(
            ReplacementTransform(eigenvector_title, eigenvalue_title),
            ReplacementTransform(equation, MathTex("A\\vec{v} = \\lambda\\vec{v}").scale(1.2).next_to(eigenvalue_title, DOWN)),
            run_time=0.8
        )
        self.wait(0.3)
        
        # Emphasize the scaling factors (eigenvalues)
        self.play(
            Write(x_eigenvalue_label),
            Flash(transformed_x, color=x_eigenvector_color, flash_radius=0.3),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            Write(y_eigenvalue_label),
            Flash(transformed_y, color=y_eigenvector_color, flash_radius=0.3),
            run_time=1
        )
        self.wait(0.5)
        
        # Visualize the scaling directly
        scaling_desc_x = Text("Scaled by 2×", font_size=20, color=x_eigenvector_color).next_to(
            x_eigenvalue_label, DOWN, buff=0.3
        )
        
        scaling_desc_y = Text("Scaled by 3×", font_size=20, color=y_eigenvector_color).next_to(
            y_eigenvalue_label, DOWN, buff=0.3
        )
        
        self.play(
            Write(scaling_desc_x),
            Write(scaling_desc_y),
            run_time=1
        )
        self.wait(0.5)
        
        #############################
        # PART 5: Conclusion (12-15s)
        #############################
        
        # Create conclusion text
        conclusion = Text(
            "Eigenvalues: How much a transformation stretches in key directions",
            font_size=28
        ).to_edge(DOWN, buff=0.5)
        
        # Zoom out slightly to see the full picture
        self.play(
            self.camera.frame.animate.scale(1.1),
            run_time=1
        )
        self.wait(0.5)
        
        # Show the concluding message
        self.play(Write(conclusion), run_time=1.5)
        self.wait(0.5)
        
        # Final animation showing the transformation again
        reset_grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(0.8)
        reset_grid.set_opacity(0.3)
        
        reset_square = Square(side_length=2, color=square_color, fill_opacity=0.5).scale(0.8)
        
        self.play(
            ReplacementTransform(grid, reset_grid),
            ReplacementTransform(square, reset_square),
            FadeOut(transformed_x),
            FadeOut(transformed_y),
            FadeOut(original_x),
            FadeOut(original_y),
            run_time=1
        )
        self.wait(0.5)
        
        # Reintroduce the eigenvectors
        final_eigenvector_x = Arrow(
            axes.c2p(0, 0), axes.c2p(2, 0), 
            color=x_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        final_eigenvector_y = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 2), 
            color=y_eigenvector_color, 
            buff=0, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            Create(final_eigenvector_x),
            Create(final_eigenvector_y),
            run_time=0.8
        )
        self.wait(0.3)
        
        # Apply the final transformation to show everything together
        self.play(
            ApplyMatrix(transformation_matrix, reset_grid),
            ApplyMatrix(transformation_matrix, reset_square),
            ReplacementTransform(
                final_eigenvector_x,
                Arrow(
                    axes.c2p(0, 0), axes.c2p(4, 0), 
                    color=x_eigenvector_color, 
                    buff=0, 
                    stroke_width=4,
                    max_tip_length_to_length_ratio=0.15
                )
            ),
            ReplacementTransform(
                final_eigenvector_y,
                Arrow(
                    axes.c2p(0, 0), axes.c2p(0, 6), 
                    color=y_eigenvector_color, 
                    buff=0, 
                    stroke_width=4,
                    max_tip_length_to_length_ratio=0.15
                )
            ),
            run_time=2
        )
        
        # Hold the final frame to allow viewers to absorb the concept
        self.wait(1.5)

if __name__ == "__main__":
    scene = EigenvectorAnimation()
    scene.render()