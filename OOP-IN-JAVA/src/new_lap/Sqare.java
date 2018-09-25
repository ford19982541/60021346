package new_lap;

import java.awt.Graphics;
import javax.swing.JPanel;
public class Sqare extends JPanel implements Shape{
	public void paintComponent(Graphics g) {
		g.drawRect(150,150,300,300);
	}
}
