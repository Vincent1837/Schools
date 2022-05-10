package stu_110502567.p11_110502567;


import javafx.fxml.FXML;


public class MenuController {

    @FXML
    protected void onStartButtonClick() {
        HelloApplication.mazeScene.getRoot().requestFocus();
        HelloApplication.currentStage.setScene(HelloApplication.mazeScene);
    }

    @FXML
    protected void onLeaveButtonClick() {
        HelloApplication.currentStage.close();
    }

}