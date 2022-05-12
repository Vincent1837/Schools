package stu_110502567;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;

public class GreedySnakeController {
    int headRow, headColumn, bodyRow, bodyColumn;
    char direction = ' ';

    @FXML
    private Pane Head;

    @FXML
    private Pane Body;

    @FXML
    private Label win;

    @FXML
    protected void onBackButtonClick() {
        HelloApplication.currentStage.setScene(HelloApplication.menuScene);
    }

    @FXML
    public void initialize() {
        Head.setStyle("-fx-background-color: black;");
        Body.setStyle("-fx-background-color: black;");
        headRow = 0;
        headColumn = 0;
        bodyRow = 0;
        bodyColumn = 0;
        direction = ' ';
        win.setVisible(false);
        GridPane.setRowIndex(Head, 0);
        GridPane.setColumnIndex(Head, 0);
    }

    @FXML
    public void handle(KeyEvent e) {
        System.out.println(e.getCode());

        if (headRow == 4 && headColumn == 4) {
            win.setVisible(true);
        } else {
            if (e.getCode() == KeyCode.DOWN && headRow < 4 && direction != 'n') {
                direction = 's';
                bodyRow = headRow++;
                bodyColumn = headColumn;
            } else if (e.getCode() == KeyCode.RIGHT && headColumn < 4 && direction != 'w') {
                direction = 'e';
                bodyColumn = headColumn++;
                bodyRow = headRow;
            } else if  (e.getCode() == KeyCode.UP && headRow > 0 && direction != 's') {
                direction = 'n';
                bodyRow = headRow--;
                bodyColumn = headColumn;
            } else if (e.getCode() == KeyCode.LEFT && headColumn > 0 && direction != 'e') {
                direction = 'w';
                bodyColumn = headColumn--;
                bodyRow = headRow;
            }
        }

        if (e.getCode() == KeyCode.SPACE) {
            initialize();
        }

        if (headRow == 4 && headColumn == 4) {
            win.setVisible(true);
        }

        GridPane.setRowIndex(Head, headRow);
        GridPane.setColumnIndex(Head, headColumn);
        GridPane.setRowIndex(Body, bodyRow);
        GridPane.setColumnIndex(Body, bodyColumn);
    }
}