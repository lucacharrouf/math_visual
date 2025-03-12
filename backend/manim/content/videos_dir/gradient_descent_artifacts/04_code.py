from manim import *
import numpy as np

class GradientDescentVisualization(Scene):
    def construct(self):
        """
        This animation visualizes the gradient descent algorithm, showing how it
        iteratively approaches the minimum of a cost function.
        """
        # Set up the coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 16, 4],
            axis_config={"color": BLUE},
            x_length=10,
            y_length=6,
        ).to_edge(DOWN, buff=0.5)
        
        # Add labels to the axes
        x_label = axes.get_x_axis_label(r"x")
        y_label = axes.get_y_axis_label(r"f(x)")
        labels = VGroup(x_label, y_label)
        
        # Define our cost function: f(x) = x^2
        def func(x):
            return x**2
        
        # Plot the function
        graph = axes.plot(func, color=BLUE)
        graph_label = MathTex(r"f(x) = x^2").next_to(graph, UP, buff=0.2).to_edge(RIGHT)
        
        # Introduction title
        title = Text("Gradient Descent Algorithm").scale(1.2).to_edge(UP)
        
        # Introduction description
        description = Text(
            "An optimization algorithm to find the minimum of a function",
            font_size=24
        ).next_to(title, DOWN)
        
        # Display introduction
        self.play(Write(title))
        self.play(Write(description))
        self.wait(2)
        
        # Transition to the main visualization
        self.play(
            FadeOut(description),
            title.animate.scale(0.7).to_corner(UL),
            Create(axes),
            Write(labels),
        )
        self.play(Create(graph), Write(graph_label))
        self.wait(1)
        
        # Explain gradient descent
        gradient_desc = Text(
            "Gradient descent uses the derivative (slope) to find the minimum", 
            font_size=24
        ).next_to(axes, UP, buff=0.2)
        
        self.play(Write(gradient_desc))
        self.wait(2)
        
        # Show the gradient calculation
        x_start = 3.5  # Starting point
        point = axes.coords_to_point(x_start, func(x_start))
        dot = Dot(point, color=RED)
        
        # Label for the starting point
        start_label = MathTex(r"x_0 = 3.5").next_to(dot, UR, buff=0.2)
        
        self.play(FadeOut(gradient_desc))
        self.play(Create(dot), Write(start_label))
        self.wait(1)
        
        # Show gradient at current point
        slope = 2 * x_start  # Derivative of x^2 is 2x
        gradient_vector = Arrow(
            start=point,
            end=point + np.array([0, -slope, 0]),
            buff=0,
            color=GREEN,
            max_tip_length_to_length_ratio=0.15,
            max_stroke_width_to_length_ratio=5
        )
        gradient_label = MathTex(r"\nabla f(x_0) = 2x_0 = 7").next_to(gradient_vector, RIGHT, buff=0.2)
        
        self.play(
            Create(gradient_vector),
            Write(gradient_label)
        )
        self.wait(1)
        
        # Explain gradient descent formula
        formula = MathTex(
            r"x_{t+1} = x_t - \alpha \nabla f(x_t)",
            font_size=36
        ).next_to(title, DOWN).to_edge(UP)
        formula_explanation = Text(
            "Where α is the learning rate", 
            font_size=24
        ).next_to(formula, DOWN, buff=0.2)
        
        self.play(
            Write(formula),
            Write(formula_explanation)
        )
        self.wait(2)
        
        # Define learning rate
        learning_rate = 0.1
        learning_rate_label = MathTex(
            r"\alpha = " + str(learning_rate),
            font_size=36
        ).to_corner(UR)
        
        self.play(
            Write(learning_rate_label),
            FadeOut(gradient_label)
        )
        self.wait(1)
        
        # Perform gradient descent iterations
        iterations = 10
        path_dots = [dot]
        current_x = x_start
        step_labels = []
        
        for i in range(iterations):
            gradient = 2 * current_x
            new_x = current_x - learning_rate * gradient
            new_point = axes.coords_to_point(new_x, func(new_x))
            new_dot = Dot(new_point, color=RED)
            
            # Create arrow for the step
            step_arrow = Arrow(
                start=path_dots[-1].get_center(),
                end=new_dot.get_center(),
                buff=0,
                color=YELLOW,
                max_tip_length_to_length_ratio=0.15
            )
            
            # Create step explanation
            step_text = MathTex(
                r"x_{" + str(i+1) + r"} = " + f"{current_x:.2f} - {learning_rate} \cdot {gradient:.2f} = {new_x:.2f}",
                font_size=28
            ).to_edge(DOWN, buff=0.2)
            
            if i > 0:
                self.play(FadeOut(step_labels[-1]))
            
            self.play(
                Create(step_arrow),
                Create(new_dot),
                Write(step_text)
            )
            step_labels.append(step_text)
            
            # Show new gradient
            new_gradient = 2 * new_x
            new_gradient_vector = Arrow(
                start=new_point,
                end=new_point + np.array([0, -new_gradient, 0]),
                buff=0,
                color=GREEN,
                max_tip_length_to_length_ratio=0.15,
                max_stroke_width_to_length_ratio=5
            )
            
            self.play(Create(new_gradient_vector))
            self.wait(0.5)
            
            # Update for next iteration
            current_x = new_x
            path_dots.append(new_dot)
            
            # Clean up after a few steps to avoid clutter
            if i > 1:
                self.play(
                    FadeOut(path_dots[-3]),
                    FadeOut(new_gradient_vector)
                )
        
        # Show the minimum point
        min_point = axes.coords_to_point(0, 0)
        min_dot = Dot(min_point, color=GOLD)
        min_label = MathTex(r"\text{Minimum at } x = 0").next_to(min_dot, DOWN, buff=0.2)
        
        self.play(
            Create(min_dot),
            Write(min_label),
            FadeOut(step_labels[-1])
        )
        
        # Final summary
        summary = Text(
            "Gradient descent iteratively approaches the minimum by following the negative gradient",
            font_size=24
        ).to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeOut(learning_rate_label),
            FadeOut(start_label),
            FadeOut(formula),
            FadeOut(formula_explanation),
            Write(summary)
        )
        self.wait(2)
        
        # Show effect of different learning rates
        effects_title = Text("Effect of Learning Rate (α)", font_size=36).next_to(title, DOWN)
        
        self.play(
            FadeOut(summary),
            Write(effects_title)
        )
        self.wait(1)
        
        # Learning rate effects explanation
        lr_too_small = Text("Too small: slow convergence", font_size=24, color=BLUE).to_edge(DOWN, buff=1.0)
        lr_too_large = Text("Too large: may overshoot or diverge", font_size=24, color=RED).to_edge(DOWN, buff=0.6)
        lr_just_right = Text("Just right: efficient convergence", font_size=24, color=GREEN).to_edge(DOWN, buff=0.2)
        
        self.play(Write(lr_too_small))
        self.wait(1)
        self.play(Write(lr_too_large))
        self.wait(1)
        self.play(Write(lr_just_right))
        self.wait(2)
        
        # Conclusion
        conclusion = Text(
            "Gradient Descent is fundamental in training machine learning models",
            font_size=30
        ).to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeOut(lr_too_small),
            FadeOut(lr_too_large),
            FadeOut(lr_just_right),
            FadeOut(effects_title),
            Write(conclusion)
        )
        self.wait(3)
        
        # Final fade out
        self.play(
            FadeOut(conclusion),
            FadeOut(title),
            FadeOut(min_label),
            FadeOut(min_dot),
            FadeOut(graph_label),
            FadeOut(graph),
            FadeOut(axes),
            FadeOut(labels),
            *[FadeOut(dot) for dot in path_dots if dot in self.mobjects]
        )
        self.wait(1)