package new_lap;

import java.awt.Graphics;
import javax.swing.JPanel;

public class Ciecle extends JPanel implements Shape {
	public void paintComponent(Graphics g) {
		g.drawOval(50,50,300,300);
	}
}
