package stu_110502567.p11_110502567;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    public static Stage currentStage;
    public static Scene menuScene;
    public static Scene mazeScene;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader mazeFxmlLoader = new FXMLLoader(HelloApplication.class.getResource("maze.fxml"));
        FXMLLoader menuFxmlLoader = new FXMLLoader(HelloApplication.class.getResource("menu.fxml"));
        currentStage = stage;
        menuScene = new Scene(menuFxmlLoader.load());
        mazeScene = new Scene(mazeFxmlLoader.load());
        currentStage.setTitle("Walk to Exit");
        currentStage.setScene(menuScene);
        currentStage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}