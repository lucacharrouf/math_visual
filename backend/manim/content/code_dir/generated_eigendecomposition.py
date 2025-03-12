from manim import *
import numpy as np

class LotkaVolterraSystem(Scene):
    def construct(self):
        # Set a lighter background for better visibility
        self.camera.background_color = "#1E1E1E"
        
        # Section 1: Introduction and title
        self.introduce_concept()
        
        # Section 2: Explain the equations
        self.explain_equations()
        
        # Section 3: Explain the parameters
        self.explain_parameters()
        
        # Section 4: Show time series solution
        self.show_population_dynamics()
        
        # Section 5: Introduce phase portrait
        self.show_phase_portrait()
        
        # Section 6: Conclusion and key insights
        self.summarize()

    def introduce_concept(self):
        # Create title and subtitle
        title = Text("The Lotka-Volterra Model", font_size=60)
        subtitle = Text("Predator-Prey Population Dynamics", font_size=36)
        
        # Position subtitle below title
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Group title elements
        title_group = VGroup(title, subtitle)
        title_group.center()
        
        # Show title with fade in
        self.play(FadeIn(title, run_time=1.5))
        self.play(FadeIn(subtitle, run_time=1))
        self.wait(2)
        
        # Shrink and move title to top-left for rest of presentation
        small_title = Text("Lotka-Volterra Model", font_size=28)
        small_title.to_corner(UL, buff=0.5)
        
        self.play(
            ReplacementTransform(title_group, small_title, run_time=1.5)
        )
        self.wait(0.5)
        
        # Store the small title for later reference
        self.small_title = small_title

    def explain_equations(self):
        # Create the Lotka-Volterra differential equations with clear labels
        eq_title = Text("The Differential Equations:", font_size=36)
        eq_title.to_edge(UP).shift(DOWN * 0.5)
        
        # Create prey equation
        prey_eq = MathTex(r"\frac{dx}{dt}", r"=", r"\alpha x", r"-", r"\beta xy", font_size=48)
        prey_eq.set_color_by_tex(r"\alpha x", BLUE)
        prey_eq.set_color_by_tex(r"\beta xy", PURPLE)
        
        # Create predator equation
        predator_eq = MathTex(r"\frac{dy}{dt}", r"=", r"\gamma xy", r"-", r"\delta y", font_size=48)
        predator_eq.set_color_by_tex(r"\gamma xy", GREEN)
        predator_eq.set_color_by_tex(r"\delta y", RED)
        
        # Position equations
        prey_eq.next_to(eq_title, DOWN, buff=0.7)
        predator_eq.next_to(prey_eq, DOWN, buff=0.7)
        
        # Add variable descriptions
        var_desc = MathTex(r"x = \text{prey population}", r", y = \text{predator population}", font_size=36)
        var_desc[0].set_color(BLUE)
        var_desc[1].set_color(RED)
        var_desc.next_to(predator_eq, DOWN, buff=0.7)
        
        # Display equations
        self.play(Write(eq_title, run_time=1))
        self.wait(0.5)
        
        # Display prey equation term by term
        self.play(Write(prey_eq[0], run_time=0.7))  # dx/dt
        self.play(Write(prey_eq[1], run_time=0.5))  # =
        self.play(Write(prey_eq[2], run_time=0.7))  # alpha x
        self.play(Write(prey_eq[3], run_time=0.5))  # -
        self.play(Write(prey_eq[4], run_time=0.7))  # beta xy
        
        self.wait(1)
        
        # Display predator equation term by term
        self.play(Write(predator_eq[0], run_time=0.7))  # dy/dt
        self.play(Write(predator_eq[1], run_time=0.5))  # =
        self.play(Write(predator_eq[2], run_time=0.7))  # gamma xy
        self.play(Write(predator_eq[3], run_time=0.5))  # -
        self.play(Write(predator_eq[4], run_time=0.7))  # delta y
        
        self.wait(1)
        
        # Show variable descriptions
        self.play(Write(var_desc, run_time=1.5))
        self.wait(2)
        
        # Store equations for later reference
        self.eq_group = VGroup(eq_title, prey_eq, predator_eq, var_desc)

    def explain_parameters(self):
        # Create parameter explanation title
        param_title = Text("Parameter Meanings:", font_size=36)
        param_title.to_edge(UP).shift(DOWN * 0.5)
        
        # Create parameter explanations
        alpha_desc = Tex(r"$\alpha$: Prey growth rate (reproduction)", font_size=32)
        alpha_desc[0][:1].set_color(BLUE)
        
        beta_desc = Tex(r"$\beta$: Prey death rate due to predation", font_size=32)
        beta_desc[0][:1].set_color(PURPLE)
        
        gamma_desc = Tex(r"$\gamma$: Predator growth rate from consuming prey", font_size=32)
        gamma_desc[0][:1].set_color(GREEN)
        
        delta_desc = Tex(r"$\delta$: Predator death rate (natural mortality)", font_size=32)
        delta_desc[0][:1].set_color(RED)
        
        # Position parameter descriptions in a column
        alpha_desc.next_to(param_title, DOWN, buff=0.5)
        beta_desc.next_to(alpha_desc, DOWN, buff=0.4)
        gamma_desc.next_to(beta_desc, DOWN, buff=0.4)
        delta_desc.next_to(gamma_desc, DOWN, buff=0.4)
        
        # Group all parameter descriptions
        param_group = VGroup(param_title, alpha_desc, beta_desc, gamma_desc, delta_desc)
        
        # Fade out equations and fade in parameter explanations
        self.play(
            FadeOut(self.eq_group, run_time=1),
            FadeIn(param_title, run_time=1)
        )
        
        # Display parameter explanations one by one
        self.play(FadeIn(alpha_desc, run_time=0.8))
        self.wait(0.7)
        self.play(FadeIn(beta_desc, run_time=0.8))
        self.wait(0.7)
        self.play(FadeIn(gamma_desc, run_time=0.8))
        self.wait(0.7)
        self.play(FadeIn(delta_desc, run_time=0.8))
        self.wait(2)
        
        # Add ecological example
        example = Text("Example: Rabbits (prey) and Foxes (predators)", font_size=28, color=YELLOW)
        example.next_to(param_group, DOWN, buff=0.6)
        
        self.play(Write(example, run_time=1.5))
        self.wait(2)
        
        # Fade out parameter explanations
        self.play(
            FadeOut(param_group, run_time=1),
            FadeOut(example, run_time=1)
        )
        self.wait(0.5)

    def show_population_dynamics(self):
        # Create section title
        dynamics_title = Text("Population Dynamics Over Time", font_size=36)
        dynamics_title.to_edge(UP).shift(DOWN * 0.5)
        
        # Create simplified equations as reminder
        prey_simple = MathTex(r"\frac{dx}{dt} = \alpha x - \beta xy", font_size=28)
        predator_simple = MathTex(r"\frac{dy}{dt} = \gamma xy - \delta y", font_size=28)
        
        equations = VGroup(prey_simple, predator_simple).arrange(DOWN, buff=0.3)
        equations.to_corner(UL, buff=1).shift(DOWN)
        
        # Create time series axes
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=4,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        
        # Add labels to axes
        x_label = Text("Time", font_size=24)
        y_label = Text("Population", font_size=24)
        
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        # Position the graph
        axes_group = VGroup(axes, x_label, y_label)
        axes_group.center().shift(DOWN * 0.5)
        
        # Define the population functions (simplified Lotka-Volterra solution)
        # For visualization purposes using predetermined functions that show the oscillating pattern
        def prey_population(t):
            return 4 + 3 * np.sin(t * 1.1 + 0.5) + 0.5 * np.sin(2.2 * t)
            
        def predator_population(t):
            return 4 + 3 * np.sin(t * 1.1 - 1) + 0.5 * np.sin(2.2 * t - 0.5)
        
        # Create the population curves
        prey_curve = axes.plot_parametric_curve(
            lambda t: [t, prey_population(t)],
            t_range=[0, 20],
            color=BLUE
        )
        
        predator_curve = axes.plot_parametric_curve(
            lambda t: [t, predator_population(t)],
            t_range=[0, 20],
            color=RED
        )
        
        # Create legend
        prey_dot = Dot(color=BLUE)
        prey_label = Text("Prey (x)", font_size=24, color=BLUE)
        prey_legend = VGroup(prey_dot, prey_label).arrange(RIGHT, buff=0.2)
        
        predator_dot = Dot(color=RED)
        predator_label = Text("Predators (y)", font_size=24, color=RED)
        predator_legend = VGroup(predator_dot, predator_label).arrange(RIGHT, buff=0.2)
        
        legend = VGroup(prey_legend, predator_legend).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UR, buff=0.5).shift(DOWN)
        
        # Show the section title and equations
        self.play(Write(dynamics_title, run_time=1))
        self.play(FadeIn(equations, run_time=1.5))
        self.wait(1)
        
        # Show the coordinate system
        self.play(
            Create(axes, run_time=1.5),
            FadeIn(x_label, run_time=1),
            FadeIn(y_label, run_time=1)
        )
        self.wait(0.5)
        
        # Show the legend
        self.play(FadeIn(legend, run_time=1))
        
        # Draw the population curves
        self.play(
            Create(prey_curve, run_time=3.5),
            Create(predator_curve, run_time=3.5)
        )
        self.wait(1)
        
        # Add annotations explaining the cycle
        cycle_arrow = CurvedArrow(
            start_point=axes.c2p(8, prey_population(8)),
            end_point=axes.c2p(12, prey_population(12)),
            angle=-TAU/4
        )
        
        cycle_text = Text("Cyclical Pattern", font_size=24, color=YELLOW)
        cycle_text.next_to(cycle_arrow, UP)
        
        self.play(
            Create(cycle_arrow, run_time=1.5),
            Write(cycle_text, run_time=1.5)
        )
        self.wait(2)
        
        # Highlight prey peak followed by predator peak
        prey_peak_dot = Dot(axes.c2p(4.5, prey_population(4.5)), color=BLUE)
        prey_peak_label = Text("Prey Peak", font_size=20, color=BLUE)
        prey_peak_label.next_to(prey_peak_dot, UP)
        
        predator_peak_dot = Dot(axes.c2p(6.5, predator_population(6.5)), color=RED)
        predator_peak_label = Text("Predator Peak", font_size=20, color=RED)
        predator_peak_label.next_to(predator_peak_dot, UP)
        
        delay_arrow = Arrow(prey_peak_dot.get_center(), predator_peak_dot.get_center(), buff=0.1)
        delay_text = Text("Time Delay", font_size=20)
        delay_text.next_to(delay_arrow, UP)
        
        self.play(
            FadeIn(prey_peak_dot, run_time=0.8),
            Write(prey_peak_label, run_time=0.8)
        )
        self.wait(0.7)
        
        self.play(
            FadeIn(predator_peak_dot, run_time=0.8),
            Write(predator_peak_label, run_time=0.8)
        )
        self.wait(0.7)
        
        self.play(
            Create(delay_arrow, run_time=1),
            Write(delay_text, run_time=1)
        )
        
        self.wait(2)
        
        # Store the time series elements
        self.time_series_group = VGroup(
            dynamics_title, equations, axes_group, 
            prey_curve, predator_curve, legend,
            cycle_arrow, cycle_text,
            prey_peak_dot, prey_peak_label,
            predator_peak_dot, predator_peak_label,
            delay_arrow, delay_text
        )

    def show_phase_portrait(self):