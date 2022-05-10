package stu_110502567.p11_110502567;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;

public class MazeController {
    int rowIndex;
    int columnIndex;


    @FXML
    private Pane man;

    @FXML
    private Label win;

    @FXML
    protected void onBackButtonClick() {
        HelloApplication.currentStage.setScene(HelloApplication.menuScene);
    }

    @FXML
    public void handle(KeyEvent e) {
        System.out.println(e.getCode());

        if (rowIndex == 4 && columnIndex == 4) {
            win.setVisible(true);
        } else {
            if (e.getCode() == KeyCode.DOWN && rowIndex < 4) {
                rowIndex++;
            } else if (e.getCode() == KeyCode.RIGHT && columnIndex < 4) {
                columnIndex++;
            } else if  (e.getCode() == KeyCode.UP && rowIndex > 0) {
                rowIndex--;
            } else if (e.getCode() == KeyCode.LEFT && columnIndex > 0) {
                columnIndex--;
            }
        }

        if (e.getCode() == KeyCode.SPACE) {
            win.setVisible(false);
            GridPane.setRowIndex(man, 0);
            GridPane.setColumnIndex(man, 0);
            rowIndex = 0;
            columnIndex = 0;
        }

        if (rowIndex == 4 && columnIndex == 4) {

            win.setVisible(true);
        }

        GridPane.setRowIndex(man, rowIndex);
        GridPane.setColumnIndex(man, columnIndex);

    }
}