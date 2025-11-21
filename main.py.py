# Person 5's File - The Integrator
import gui
import logic
import word_manager

if __name__ == "__main__":
    # 1. Get the movie
    movie = word_manager.get_random_movie()
    
    # 2. Start the logic
    game = logic.GameLogic(movie)
    
    # 3. Start the GUI, passing the logic engine to it
    app = gui.GameWindow(game)
    
    # 4. Run the app
    app.mainloop()
