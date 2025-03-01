from manim import *

class EigenvaluesAndEigenvectors(Scene):
    def construct(self):
        # Define colors for consistency
        title_color = BLUE
        vector_color = RED
        eigenvector1_color = GREEN
        eigenvector2_color = BLUE
        matrix_color = YELLOW
        equation_color = WHITE
        
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GRAY},
            x_length=6,
            y_length=6,
        ).add_coordinates()
        axes.to_edge(LEFT, buff=1)
        
        # Our transformation matrix A
        matrix_A = np.array([[2, 0], [0, 3]])
        
        # SECTION 1: Introduction and Setup
        # Educational purpose: Establish the visual space and introduce the concept
        
        # Animate the coordinate system appearing
        self.play(Create(axes), run_time=1)
        
        # Create the initial vector v = [1, 1]
        vector_v = Vector([1, 1], color=vector_color)
        vector_v.shift(axes.get_origin())
        vector_label = MathTex("\\vec{v}", color=vector_color).next_to(vector_v.get_end(), RIGHT)
        
        # Show the vector
        self.play(Create(vector_v), Write(vector_label), run_time=1)
        
        # Display title
        title = Text("Eigenvalues & Eigenvectors", color=title_color)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        
        # SECTION 2: Show the matrix and its effect on a regular vector
        # Educational purpose: Demonstrate how matrices transform vectors generally
        
        # Show the matrix A
        matrix_tex = MathTex(
            "A = \\begin{bmatrix} 2 & 0 \\\\ 0 & 3 \\end{bmatrix}",
            color=matrix_color
        )
        matrix_tex.to_corner(UR)
        self.play(Write(matrix_tex), run_time=1)
        
        # Create the transformed vector Av
        transformed_vector = Vector([2, 3], color=vector_color)
        transformed_vector.shift(axes.get_origin())
        transformed_label = MathTex("A\\vec{v}", color=vector_color).next_to(transformed_vector.get_end(), RIGHT)
        
        # Add a note about what's happening
        transform_note = Text("Matrix A transforms the vector", font_size=24)
        transform_note.next_to(matrix_tex, DOWN, buff=0.5)
        
        # Animate the transformation
        self.play(Write(transform_note), run_time=0.5)
        self.wait(0.5)
        
        # Show the transformation effect using ApplyMatrix
        self.play(
            ApplyMatrix(matrix_A, vector_v),
            Transform(vector_v, transformed_vector),
            Transform(vector_label, transformed_label),
            run_time=2
        )
        self.wait(1)
        
        # Clear the scene except for the coordinate system and title
        self.play(
            FadeOut(vector_v),
            FadeOut(vector_label),
            FadeOut(transform_note),
            run_time=0.5
        )
        
        # SECTION 3: Introduce eigenvectors
        # Educational purpose: Show what makes eigenvectors special
        
        # Create two special vectors: eigenvectors
        eigenvector1 = Vector([1, 0], color=eigenvector1_color)
        eigenvector2 = Vector([0, 1], color=eigenvector2_color)
        eigenvector1.shift(axes.get_origin())
        eigenvector2.shift(axes.get_origin())
        
        # Labels for eigenvectors
        eigenvector1_label = MathTex("\\vec{v}_1", color=eigenvector1_color).next_to(eigenvector1.get_end(), RIGHT)
        eigenvector2_label = MathTex("\\vec{v}_2", color=eigenvector2_color).next_to(eigenvector2.get_end(), UP)
        
        # Show the eigenvectors
        self.play(
            Create(eigenvector1),
            Create(eigenvector2),
            Write(eigenvector1_label),
            Write(eigenvector2_label),
            run_time=1
        )
        
        # Add text explaining these are special vectors
        special_text = Text("Special vectors: eigenvectors", font_size=30)
        special_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(special_text), run_time=1)
        
        # SECTION 4: Demonstrate the first eigenvector transformation
        # Educational purpose: Show how eigenvectors maintain direction under transformation
        
        # Create the transformed eigenvector1
        transformed_eigenvector1 = Vector([2, 0], color=eigenvector1_color)
        transformed_eigenvector1.shift(axes.get_origin())
        transformed_eigenvector1_label = MathTex("A\\vec{v}_1", color=eigenvector1_color).next_to(transformed_eigenvector1.get_end(), RIGHT)
        
        # Animate the transformation of the first eigenvector
        self.play(
            ApplyMatrix(matrix_A, eigenvector1),
            Transform(eigenvector1, transformed_eigenvector1),
            Transform(eigenvector1_label, transformed_eigenvector1_label),
            run_time=1
        )
        
        # Show the eigenvalue
        eigenvalue1_text = MathTex("\\lambda_1 = 2", color=eigenvector1_color)
        eigenvalue1_text.next_to(special_text, DOWN, buff=0.5)
        self.play(Write(eigenvalue1_text), run_time=1)
        
        # Explain what's happening
        note1 = Text("Direction unchanged, length multiplied by 2", font_size=24, color=eigenvector1_color)
        note1.next_to(eigenvalue1_text, DOWN, buff=0.3)
        self.play(Write(note1), run_time=1)
        self.wait(0.5)
        
        # SECTION 5: Demonstrate the second eigenvector transformation
        # Educational purpose: Reinforce concept with a different eigenvector/eigenvalue
        
        # Create the transformed eigenvector2
        transformed_eigenvector2 = Vector([0, 3], color=eigenvector2_color)
        transformed_eigenvector2.shift(axes.get_origin())
        transformed_eigenvector2_label = MathTex("A\\vec{v}_2", color=eigenvector2_color).next_to(transformed_eigenvector2.get_end(), UP)
        
        # Animate the transformation of the second eigenvector
        self.play(
            ApplyMatrix(matrix_A, eigenvector2),
            Transform(eigenvector2, transformed_eigenvector2),
            Transform(eigenvector2_label, transformed_eigenvector2_label),
            run_time=1
        )
        
        # Show the eigenvalue
        eigenvalue2_text = MathTex("\\lambda_2 = 3", color=eigenvector2_color)
        eigenvalue2_text.next_to(eigenvalue1_text, DOWN, buff=1.2)  # Position it below note1
        self.play(Write(eigenvalue2_text), run_time=1)
        
        # Explain what's happening
        note2 = Text("Direction unchanged, length multiplied by 3", font_size=24, color=eigenvector2_color)
        note2.next_to(eigenvalue2_text, DOWN, buff=0.3)
        self.play(Write(note2), run_time=1)
        self.wait(0.5)
        
        # SECTION 6: Show the defining equation
        # Educational purpose: Connect visual understanding to mathematical representation
        
        # Move matrix_tex to make room for the equation
        self.play(matrix_tex.animate.to_edge(RIGHT, buff=1), run_time=0.5)
        
        # Create the eigenvalue equation
        eigenvalue_equation = MathTex(
            "A", "\\vec{v}", "=", "\\lambda", "\\vec{v}",
            tex_to_color_map={
                "A": matrix_color,
                "\\vec{v}": ORANGE,
                "\\lambda": YELLOW
            }
        )
        eigenvalue_equation.next_to(matrix_tex, DOWN, buff=1)
        
        # Animate the equation appearing
        self.play(Write(eigenvalue_equation), run_time=1)
        
        # Highlight parts of the equation
        for i in [0, 1, 3, 4]:
            self.play(Indicate(eigenvalue_equation[i]), run_time=0.5)
        
        # SECTION 7: Conclusion
        # Educational purpose: Summarize the key concept for retention
        
        # Final explanation text
        conclusion = Text(
            "Eigenvalues (λ) tell us how much eigenvectors\nstretch under transformation",
            font_size=28
        )
        conclusion.to_edge(DOWN, buff=0.7)
        self.play(Write(conclusion), run_time=2)
        
        # Final pause
        self.wait(1)

if __name__ == "__main__":
    scene = EigenvaluesAndEigenvectors()
    scene.render()