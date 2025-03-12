from manim import *
import numpy as np

class EigenvectorsAnimation(Scene):
    def construct(self):
        # Set up the coordinate system with a light gray grid
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GRAY},
        )
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            }
        )
        
        # Define our transformation matrix
        transformation_matrix = np.array([
            [2, 1],
            [1, 2]
        ])
        
        # Matrix to display on screen
        matrix_tex = MathTex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}").scale(0.8)
        matrix_tex.to_corner(UR)
        
        # Define vectors
        regular_vector = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1, 1), 
                             color=RED, buff=0, stroke_width=4)
        regular_vector_label = MathTex("v", color=RED).next_to(regular_vector.get_end(), UP+RIGHT, buff=0.1).scale(0.8)
        
        eigenvector1 = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1, 1), 
                           color=BLUE, buff=0, stroke_width=4)
        eigenvector1_label = MathTex("e_1", color=BLUE).next_to(eigenvector1.get_end(), UP+RIGHT, buff=0.1).scale(0.8)
        
        eigenvector2 = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1, -1), 
                           color=GREEN, buff=0, stroke_width=4)
        eigenvector2_label = MathTex("e_2", color=GREEN).next_to(eigenvector2.get_end(), DOWN+RIGHT, buff=0.1).scale(0.8)
        
        eigenvalue1 = MathTex(r"\lambda_1 = 3", color=BLUE).to_corner(UL).scale(0.8)
        eigenvalue2 = MathTex(r"\lambda_2 = 1", color=GREEN).next_to(eigenvalue1, DOWN).scale(0.8)
        
        # Text explanations
        intro_text = Text("When a transformation happens...", font_size=32).to_edge(DOWN, buff=0.5)
        reg_vector_text = Text("Most vectors change BOTH direction and length", font_size=32).to_edge(DOWN, buff=0.5)
        eigen_intro_text = Text("Eigenvectors are special vectors that...", font_size=32).to_edge(DOWN, buff=0.5)
        eigen_property_text = Text("...only change in LENGTH, not direction", font_size=32).to_edge(DOWN, buff=0.5)
        final_text = Text("Eigenvectors reveal the skeleton of transformations", font_size=32).to_edge(DOWN, buff=0.5)
        
        # 0-3 seconds: Initial setup
        self.play(
            Create(grid),
            Create(axes),
            run_time=1
        )
        
        self.play(
            GrowArrow(regular_vector),
            Write(regular_vector_label),
            run_time=0.5
        )
        
        self.play(
            Write(intro_text),
            FadeIn(matrix_tex),
            run_time=1.5
        )
        
        # 3-6 seconds: Apply transformation to regular vector
        # Create a copy of the grid to transform
        transformed_grid = grid.copy()
        
        # Calculate the transformed vector
        regular_vec_array = np.array([1, 1])
        transformed_vec_array = transformation_matrix @ regular_vec_array
        
        transformed_vector = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(transformed_vec_array[0], transformed_vec_array[1]),
            color=RED, buff=0, stroke_width=4
        )
        
        transformed_vector_label = MathTex("v", color=RED).next_to(
            transformed_vector.get_end(), UP+RIGHT, buff=0.1
        ).scale(0.8)
        
        # Create transformation path for animation
        n_points = 30
        path_points = []
        for i in range(n_points + 1):
            t = i / n_points
            interpolated_matrix = (1-t) * np.eye(2) + t * transformation_matrix
            current_vec = interpolated_matrix @ regular_vec_array
            path_points.append(axes.coords_to_point(current_vec[0], current_vec[1]))
        
        vector_path = VMobject(stroke_width=2, stroke_color=RED, stroke_opacity=0.3)
        vector_path.set_points_smoothly(path_points)
        
        # Apply the transformation
        self.play(
            transformed_grid.animate.apply_matrix(transformation_matrix),
            Transform(regular_vector, transformed_vector),
            Transform(regular_vector_label, transformed_vector_label),
            FadeTransform(intro_text, reg_vector_text), 
            Create(vector_path),
            run_time=3
        )
        
        # 6-9 seconds: Reset and introduce eigenvector 1
        self.play(
            FadeOut(regular_vector),
            FadeOut(regular_vector_label),
            FadeOut(reg_vector_text),
            FadeOut(vector_path),
            Transform(transformed_grid, grid),
            run_time=1.5
        )
        
        self.play(
            GrowArrow(eigenvector1),
            Write(eigenvector1_label),
            run_time=0.75
        )
        
        # Make eigenvector pulse to draw attention
        self.play(
            eigenvector1.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            eigenvector1.animate.scale(1/1.2),
            run_time=0.5
        )
        
        self.play(
            Write(eigen_intro_text),
            run_time=0.75
        )
        
        # 9-12 seconds: Apply transformation to eigenvector 1
        # Calculate the transformed eigenvector
        eigen1_vec_array = np.array([1, 1])
        transformed_eigen1_array = transformation_matrix @ eigen1_vec_array
        
        # The eigenvector should scale by eigenvalue (3) but keep same direction
        transformed_eigenvector1 = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(3, 3),  # λ₁ = 3 times the original
            color=BLUE, buff=0, stroke_width=4
        )
        
        transformed_eigenvector1_label = MathTex("e_1", color=BLUE).next_to(
            transformed_eigenvector1.get_end(), UP+RIGHT, buff=0.1
        ).scale(0.8)
        
        transformed_grid2 = grid.copy()
        
        self.play(
            transformed_grid2.animate.apply_matrix(transformation_matrix),
            Transform(eigenvector1, transformed_eigenvector1),
            Transform(eigenvector1_label, transformed_eigenvector1_label),
            FadeTransform(eigen_intro_text, eigen_property_text),
            FadeIn(eigenvalue1),
            run_time=3
        )
        
        # 12-15 seconds: Introduce second eigenvector
        self.play(
            GrowArrow(eigenvector2),
            Write(eigenvector2_label),
            FadeIn(eigenvalue2),
            run_time=1
        )
        
        # For eigenvector2, λ₂ = 1, so it doesn't change length
        transformed_eigenvector2 = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, -1),  # λ₂ = 1, so same as original
            color=GREEN, buff=0, stroke_width=4
        )
        
        transformed_eigenvector2_label = MathTex("e_2", color=GREEN).next_to(
            transformed_eigenvector2.get_end(), DOWN+RIGHT, buff=0.1
        ).scale(0.8)
        
        self.play(
            Transform(eigenvector2, transformed_eigenvector2),
            Transform(eigenvector2_label, transformed_eigenvector2_label),
            FadeTransform(eigen_property_text, final_text),
            run_time=2
        )
        
        # Final pulse of both eigenvectors
        self.play(
            eigenvector1.animate.scale(1.2),
            eigenvector2.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            eigenvector1.animate.scale(1/1.2),
            eigenvector2.animate.scale(1/1.2),
            run_time=0.5
        )
        
        self.wait(1)