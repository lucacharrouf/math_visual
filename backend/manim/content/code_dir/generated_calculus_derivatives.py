from manim import *

class DerivativeVisualization(Scene):
    def construct(self):
        # Set up the main coordinate plane for f(x) = x²
        plane1 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"include_numbers": True},
            x_length=10,
            y_length=5
        ).shift(UP * 1.5)
        
        # Label for the original function
        func_label = MathTex("f(x) = x^2").next_to(plane1, UP).set_color(BLUE)
        
        # Create the parabola function
        def parabola(t):
            return plane1.coords_to_point(t, t**2)
        
        parabola_graph = ParametricFunction(parabola, t_range=[-3, 3, 0.01], color=BLUE)
        
        # Add coordinate plane and parabola to the scene
        self.play(
            Create(plane1),
            Write(func_label),
        )
        self.play(Create(parabola_graph), run_time=2)
        self.wait(0.5)
        
        # Create a tracker for the x-value of our moving point
        x_tracker = ValueTracker(-2)
        
        # Create the main point P that moves along the curve
        point_p = Dot(color=RED)
        point_p.add_updater(
            lambda m: m.move_to(parabola(x_tracker.get_value()))
        )
        
        # Create the secant points and lines
        secant_point1 = Dot(color=RED_A)
        secant_point2 = Dot(color=RED_A)
        
        # Initial distance for secant points (will converge later)
        delta = 0.5
        
        secant_point1.add_updater(
            lambda m: m.move_to(parabola(x_tracker.get_value() - delta))
        )
        secant_point2.add_updater(
            lambda m: m.move_to(parabola(x_tracker.get_value() + delta))
        )
        
        # Secant lines from the adjacent points to point P
        secant_line1 = Line(color=RED)
        secant_line2 = Line(color=RED)
        
        secant_line1.add_updater(
            lambda m: m.put_start_and_end_on(
                secant_point1.get_center(), point_p.get_center()
            )
        )
        secant_line2.add_updater(
            lambda m: m.put_start_and_end_on(
                point_p.get_center(), secant_point2.get_center()
            )
        )
        
        # Add point P and secant elements
        self.play(FadeIn(point_p))
        avg_rate_text = Text("Average Rate of Change", font_size=24).to_edge(UP)
        
        self.play(
            FadeIn(secant_point1),
            FadeIn(secant_point2),
            FadeIn(secant_line1),
            FadeIn(secant_line2),
            Write(avg_rate_text)
        )
        
        # Move point P along the curve
        self.play(x_tracker.animate.set_value(0), rate_func=linear, run_time=3)
        
        # Create tangent line (it will replace the secant lines)
        tangent_line = Line(color=RED)
        
        def update_tangent(line):
            x = x_tracker.get_value()
            # Calculate tangent slope at point x (derivative of x² is 2x)
            slope = 2 * x
            
            # Get the current point on the curve
            point = parabola(x)
            
            # Create points for the tangent line
            x_diff = 1  # How far to extend the tangent line
            tan_x1 = x - x_diff
            tan_y1 = x**2 + slope * (tan_x1 - x)
            tan_x2 = x + x_diff
            tan_y2 = x**2 + slope * (tan_x2 - x)
            
            # Set the tangent line positions
            line.put_start_and_end_on(
                plane1.coords_to_point(tan_x1, tan_y1),
                plane1.coords_to_point(tan_x2, tan_y2)
            )
            return line
        
        tangent_line.add_updater(update_tangent)
        
        # Converge the secant lines to the tangent line by reducing delta
        inst_rate_text = Text("Instantaneous Rate of Change = Derivative", font_size=24).to_edge(UP)
        
        # Make secant lines converge to tangent line
        self.play(
            Transform(avg_rate_text, inst_rate_text),
            run_time=1
        )
        
        # Animation for secant lines converging to tangent
        def delta_updater(dt):
            nonlocal delta
            if delta > 0.01:
                delta -= dt * 0.5  # Gradually reduce delta
        
        self.add(tangent_line)
        self.play(
            UpdateFromAlphaFunc(
                secant_line1, 
                lambda m, a: m.set_opacity(1 - a)
            ),
            UpdateFromAlphaFunc(
                secant_line2, 
                lambda m, a: m.set_opacity(1 - a)
            ),
            UpdateFromAlphaFunc(
                secant_point1, 
                lambda m, a: m.set_opacity(1 - a)
            ),
            UpdateFromAlphaFunc(
                secant_point2, 
                lambda m, a: m.set_opacity(1 - a)
            ),
            run_time=2
        )
        self.remove(secant_line1, secant_line2, secant_point1, secant_point2)
        
        # Create a slope indicator (small right triangle) on the tangent line
        slope_triangle = Polygon(
            [0, 0, 0], [1, 0, 0], [1, 1, 0],
            color=YELLOW,
            fill_opacity=0.3
        ).scale(0.2)
        
        slope_value = DecimalNumber(
            0,
            num_decimal_places=1,
            include_sign=True,
            font_size=24
        )
        
        def update_slope_indicator(triangle):
            x = x_tracker.get_value()
            slope = 2 * x
            
            # Scale triangle to make it more visible when slope is small
            scale_factor = max(0.2, min(0.5, abs(slope) * 0.2))
            
            # Get a position on the tangent line
            point = parabola(x)
            
            # Calculate points for a right triangle showing the slope
            if abs(slope) < 0.1:
                # Special case for nearly horizontal tangent
                triangle.become(
                    Polygon(
                        [0, 0, 0], [0.5, 0, 0], [0.5, 0.01, 0],
                        color=YELLOW,
                        fill_opacity=0.3
                    ).scale(scale_factor).next_to(point, RIGHT + UP * slope, buff=0.1)
                )
            else:
                # Normal case - create a right triangle with the hypotenuse along the tangent
                if slope > 0:
                    triangle.become(
                        Polygon(
                            [0, 0, 0], [1, 0, 0], [1, slope, 0],
                            color=YELLOW,
                            fill_opacity=0.3
                        ).scale(scale_factor).next_to(point, RIGHT, buff=0.1)
                    )
                else:
                    triangle.become(
                        Polygon(
                            [0, 0, 0], [1, 0, 0], [1, slope, 0],
                            color=YELLOW,
                            fill_opacity=0.3
                        ).scale(scale_factor).next_to(point, LEFT, buff=0.1)
                    )
            return triangle
        
        def update_slope_value(decimal):
            x = x_tracker.get_value()
            slope = 2 * x
            decimal.set_value(slope)
            decimal.next_to(slope_triangle, RIGHT, buff=0.1)
            return decimal
        
        slope_triangle.add_updater(update_slope_indicator)
        slope_value.add_updater(update_slope_value)
        
        # Add slope indicator with its value
        self.play(
            FadeIn(slope_triangle),
            FadeIn(slope_value)
        )
        
        # Continue moving the point
        self.play(x_tracker.animate.set_value(2), rate_func=linear, run_time=4)
        
        # Set up second coordinate plane for the derivative function
        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-6, 6, 1],
            axis_config={"include_numbers": True},
            x_length=10,
            y_length=5
        ).shift(DOWN * 1.5)
        
        # Create the derivative function f'(x) = 2x
        def derivative_function(t):
            return plane2.coords_to_point(t, 2*t)
        
        derivative_graph = ParametricFunction(derivative_function, t_range=[-3, 3, 0.01], color=GREEN)
        
        # Create a point on the derivative graph that corresponds to point P
        derivative_point = Dot(color=GREEN)
        derivative_point.add_updater(
            lambda m: m.move_to(derivative_function(x_tracker.get_value()))
        )
        
        # Connecting text for the derivative
        derivative_text = Text("Derivative: f'(x) = slope at point x", font_size=24).next_to(plane2, UP)
        
        # Add the second plane and derivative elements
        self.play(
            FadeIn(plane2),
            Write(derivative_text),
            run_time=1
        )
        
        # Gradient visualization - connecting line between the planes
        connector_line = DashedLine(color=YELLOW)
        connector_line.add_updater(
            lambda m: m.put_start_and_end_on(
                point_p.get_center(),
                derivative_point.get_center()
            )
        )
        
        # Add derivative point and connecting line
        self.play(
            FadeIn(derivative_point),
            FadeIn(connector_line),
            run_time=1
        )
        
        # Draw the derivative graph
        self.play(Create(derivative_graph), run_time=2)
        
        # Final formula display
        final_formula = MathTex("f'(x) = \\frac{d}{dx}(x^2) = 2x").scale(1.2).to_edge(DOWN)
        
        self.play(Write(final_formula), run_time=1)
        
        # Final demonstration of synchronized movement
        self.play(x_tracker.animate.set_value(-2), rate_func=linear, run_time=3)
        self.play(x_tracker.animate.set_value(2), rate_func=linear, run_time=3)
        
        # Final pause to observe the complete visualization
        self.wait(2)

if __name__ == "__main__":
    scene = DerivativeVisualization()
    scene.render()