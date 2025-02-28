from manim import *

class EigenvalueEigenvectorVisual(Scene):
    def construct(self):
        # Setup the coordinate system with a light grid
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GREY},
        )
        grid = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 0.5,
                "stroke_opacity": 0.4
            }
        )
        
        # Create the scene by introducing the coordinate system
        self.play(Create(grid), Create(axes), run_time=1)
        self.wait(0.5)
        
        # Define the original vector v = [1, 2]
        vector_v = Vector([1, 2], color=RED)
        vector_v_label = MathTex("\\vec{v}", color=RED).next_to(vector_v.get_end(), UP+RIGHT, buff=0.1)
        
        # Introduce vector v
        self.play(GrowArrow(vector_v), Write(vector_v_label), run_time=1)
        self.wait(0.5)
        
        # Define the matrix A = [[2, 1], [1, 1]]
        matrix_A = Matrix([[2, 1], [1, 1]])
        matrix_A.scale(0.8).to_corner(UR, buff=1)
        matrix_A_label = Text("Matrix A", font_size=24).next_to(matrix_A, UP)
        
        # Introduce matrix A
        self.play(Write(matrix_A), Write(matrix_A_label), run_time=1)
        self.wait(0.5)
        
        # Define the transformed vector Av
        # First, calculate Av = [2, 1; 1, 1] * [1, 2] = [4, 3]
        vector_Av = Vector([4, 3], color=RED)
        vector_Av_label = MathTex("A\\vec{v}", color=RED).next_to(vector_Av.get_end(), RIGHT, buff=0.1)
        
        # Show the transformation of v by matrix A
        vector_v_faded = vector_v.copy().set_color(RED_A)
        
        # First, fade original vector to light red
        self.play(Transform(vector_v, vector_v_faded), run_time=0.5)
        
        # Then show the resulting transformed vector
        self.play(GrowArrow(vector_Av), Write(vector_Av_label), run_time=1.5)
        self.wait(0.5)
        
        # Add explanation text
        explanation_1 = Text("Most vectors change direction when transformed", 
                           font_size=28).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation_1), run_time=1)
        self.wait(1)
        
        # Introduce the eigenvector w = [1, 1]
        vector_w = Vector([1, 1], color=BLUE)
        vector_w_label = MathTex("\\vec{w}", color=BLUE).next_to(vector_w.get_end(), UP+RIGHT, buff=0.1)
        self.play(
            FadeOut(explanation_1),
            GrowArrow(vector_w),
            Write(vector_w_label),
            run_time=1
        )
        self.wait(0.5)
        
        # Add text explaining eigenvectors
        explanation_2 = Text("But special vectors only change length", 
                           font_size=28).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation_2), run_time=1)
        self.wait(0.5)
        
        # Define the transformed eigenvector Aw
        # Calculate Aw = [2, 1; 1, 1] * [1, 1] = [3, 2] = 2*[1.5, 1] = 2*[1, 1]
        vector_Aw = Vector([2, 2], color=BLUE)  # Scaled by eigenvalue 2
        vector_Aw_label = MathTex("A\\vec{w}", color=BLUE).next_to(vector_Aw.get_end(), UP+RIGHT, buff=0.1)
        
        # Show the transformation of w by matrix A
        self.play(
            FadeOut(explanation_2),
            run_time=0.5
        )
        
        # Animate the transformation showing eigenvector behavior
        self.play(
            TransformFromCopy(vector_w, vector_Aw),
            Write(vector_Aw_label),
            run_time=2
        )
        self.wait(0.5)
        
        # Highlight the eigenvalue with a label
        eigenvalue_label = MathTex("\\lambda = 2", color=YELLOW).next_to(vector_Aw, RIGHT)
        eigenvalue_highlight = SurroundingRectangle(eigenvalue_label, color=YELLOW)
        
        self.play(
            Write(eigenvalue_label),
            Create(eigenvalue_highlight),
            run_time=1
        )
        self.wait(0.5)
        
        # Display the eigenvalue equation
        eigenvalue_equation = MathTex(
            "A", "\\vec{w}", "=", "\\lambda", "\\vec{w}"
        ).to_edge(DOWN, buff=0.5)
        eigenvalue_equation[0].set_color(WHITE)  # Matrix A
        eigenvalue_equation[1].set_color(BLUE)   # Vector w
        eigenvalue_equation[3].set_color(YELLOW) # λ (eigenvalue)
        eigenvalue_equation[4].set_color(BLUE)   # Vector w again
        
        self.play(Write(eigenvalue_equation), run_time=1)
        self.wait(0.5)
        
        # Visual connection showing A*w equals lambda*w
        matrix_times_w = MathTex(
            "A", "\\vec{w}", "=", 
            "\\begin{bmatrix} 2 & 1 \\\\ 1 & 1 \\end{bmatrix}", 
            "\\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}", 
            "=", 
            "\\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}"
        ).scale(0.8).next_to(eigenvalue_equation, UP, buff=0.5)
        
        lambda_times_w = MathTex(
            "\\lambda", "\\vec{w}", "=",
            "2", "\\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}",
            "=",
            "\\begin{bmatrix} 2 \\\\ 2 \\end{bmatrix}"
        ).scale(0.8).next_to(matrix_times_w, UP, buff=0.3)
        
        # Note: For educational clarity, we use [3, 2] for Aw to show the actual result
        # and [2, 2] for λw to emphasize this is along the same direction as [1, 1]
        
        self.play(Write(matrix_times_w), run_time=1.5)
        self.wait(0.5)
        self.play(Write(lambda_times_w), run_time=1.5)
        
        # Final pause to absorb the concept
        self.wait(2)

if __name__ == "__main__":
    scene = EigenvalueEigenvectorVisual()
    scene.render()