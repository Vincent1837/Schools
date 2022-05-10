/**
 * Assignment 10
 * Student Number: 110502567
 * Course: CE_1002
 */

package com.example.a10_110502567_2;

import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    Circle circle;
    int xSpeed = 10;
    int ySpeed = 10;
    final int WIDTH = 700;
    final int HEIGHT = 600;

    @Override
    public void start(Stage stage) throws IOException {
        Pane pane  = new Pane();
        Scene scene = new Scene(pane, WIDTH, HEIGHT);
        stage.setTitle("Bounding BuBBle");
        stage.setScene(scene);
        circle = new Circle();
        circle.setRadius(40);
        circle.setFill(Paint.valueOf("ABCDEF"));
        circle.setCenterX(250);
        circle.setCenterY(50);
        pane.getChildren().add(circle);
        AnimationTimer mainTimer = new AnimationTimer() {
            @Override
            public void handle(long l) {
                update();
            }
        };
        mainTimer.start();
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    public  void update() {
        if(circle.getCenterX() + circle.getRadius() > WIDTH || circle.getCenterX() - circle.getRadius() < 0) {
            xSpeed = - xSpeed;
        }
        if(circle.getCenterY() + circle.getRadius() > HEIGHT || circle.getCenterY() - circle.getRadius() < 0) {
            ySpeed = - ySpeed;
        }
        circle.setCenterX(circle.getCenterX() + xSpeed);
        circle.setCenterY(circle.getCenterY() + ySpeed);
    }

}