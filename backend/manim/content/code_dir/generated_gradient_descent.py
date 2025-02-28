from manim import *
import numpy as np

class GradientDescentAnimation(ThreeDScene):
    def construct(self):
        # Configure the scene
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        self.camera.set_zoom(0.7)

        # Define the bowl-shaped surface function
        def surface_func(u, v):
            x = u
            y = v
            z = 0.5 * (x**2 + y**2)
            return np.array([x, y, z])

        # Create the surface with color gradient
        surface = Surface(
            lambda u, v: surface_func(u, v),
            u_range=(-3, 3),
            v_range=(-3, 3),
            resolution=(50, 50)
        )

        # Define color gradient based on height
        surface.set_fill_by_value(
            axes=ThreeDAxes(),
            colors=[(RED, -0.5), (YELLOW, 3), (BLUE, 6)],
            axis=2
        )

        # Initial position and optimization path
        start_point = np.array([-2, 2, surface_func(-2, 2)[2]])
        path_points = []
        current_point = start_point.copy()

        # Animation Phase 1: Surface Introduction (0-3s)
        self.play(
            Create(surface, run_time=2),
        )
        self.wait(0.5)

        # Create optimization point (sphere)
        sphere = Sphere(radius=0.1).move_to(start_point)
        sphere.set_color(WHITE)
        self.play(FadeIn(sphere))
        self.wait(0.5)

        # Animation Phase 2: First gradient step (3-6s)
        def get_gradient(point):
            x, y = point[0], point[1]
            return np.array([x, y, 0])  # Gradient of x²+y²

        # Create initial gradient arrow
        gradient = get_gradient(current_point[:2])
        # Use Arrow instead of Arrow3D
        normalized_gradient = gradient/np.linalg.norm(gradient)
        arrow = Arrow(
            start=current_point,
            end=current_point - 0.5 * normalized_gradient,
            color=BLUE,
            buff=0
        )
        self.play(Create(arrow))
        self.wait(0.5)

        # Animation Phase 3: Optimization steps (6-12s)
        learning_rate = 0.3
        num_steps = 20

        # Create a path to update
        path = VMobject()
        path.set_points_as_corners([current_point])
        path.set_color(PURPLE)
        self.add(path)

        for i in range(num_steps):
            # Calculate new position
            gradient = get_gradient(current_point[:2])
            step = learning_rate * gradient / (1 + i/5)  # Decreasing step size
            new_point = current_point - step
            new_point[2] = surface_func(new_point[0], new_point[1])[2]
            
            # Create new arrow
            normalized_gradient = gradient/np.linalg.norm(gradient)
            new_arrow = Arrow(
                start=new_point,
                end=new_point - 0.3 * normalized_gradient,
                color=BLUE,
                buff=0
            )

            # Update path
            new_path = VMobject()
            path_points.append(new_point)
            new_path.set_points_as_corners([p for p in path_points])
            new_path.set_color(PURPLE)

            # Animate step
            self.play(
                sphere.animate.move_to(new_point),
                Transform(arrow, new_arrow),
                Transform(path, new_path),
                run_time=0.3
            )

            current_point = new_point

        # Animation Phase 4: Highlight minimum (12-15s)
        minimum_point = Sphere(radius=0.15).move_to([0, 0, 0])
        minimum_point.set_color(RED)
        self.play(
            FadeIn(minimum_point),
            minimum_point.animate.set_opacity(0.7)
        )

        # Add title text
        title = Text("Gradient Descent", font_size=48)
        title.to_corner(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Final camera movement
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, zoom=0.8)
        self.wait(2)

if __name__ == "__main__":
    scene = GradientDescentAnimation()
    scene.render()