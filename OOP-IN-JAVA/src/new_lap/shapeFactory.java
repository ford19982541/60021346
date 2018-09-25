package new_lap;

import javax.swing.JPanel;

public class shapeFactory {
	public JPanel getShape(String ShapeType) {
		if (ShapeType == null) {
			return null;
		}
		if(ShapeType.equalsIgnoreCase("CIRCLE")) {
			return new Ciecle();
		}else if (ShapeType.equalsIgnoreCase("RECTANGLE")) {
			return new Ractangle();
		}else if (ShapeType.equalsIgnoreCase("SQUARE")) {
			return new Sqare();
		}
	
		return null;
	}

}
