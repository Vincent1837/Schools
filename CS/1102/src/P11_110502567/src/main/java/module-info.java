module com.example.p11_110502567 {
    requires javafx.controls;
    requires javafx.fxml;


    opens stu_110502567.p11_110502567 to javafx.fxml;
    exports stu_110502567.p11_110502567;
}