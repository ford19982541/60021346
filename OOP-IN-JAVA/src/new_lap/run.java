package new_lap;

import javax.swing.JPanel;

import java.awt.Container;

import javax.swing.JFrame;
public class run {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		shapeFactory objShape = new shapeFactory();
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		frame.setSize(800, 600);
		Container c = frame.getContentPane();
		c.setLayout(null);
		
		JPanel shape1 = objShape.getShape("CIRCLE");
		shape1.setSize(500,500);
		frame.add(shape1);
		
		JPanel shape2 = objShape.getShape("RECTANGLE");
		shape2.setSize(500,500);
		frame.add(shape2);
		
		frame.setVisible(true);
	}

}
