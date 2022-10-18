package stu_110502567;


import javafx.fxml.FXML;


public class MenuController {

    @FXML
    protected void onStartButtonClick() {
        HelloApplication.greedySnakeScene.getRoot().requestFocus();
        HelloApplication.currentStage.setScene(HelloApplication.greedySnakeScene);

    }

    @FXML
    protected void onLeaveButtonClick() {
        HelloApplication.currentStage.close();
    }

}