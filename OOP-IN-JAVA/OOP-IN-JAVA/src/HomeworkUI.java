import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JSplitPane;
import javax.swing.JInternalFrame;
import javax.swing.JComboBox;
import javax.swing.JToolBar;
import javax.swing.JSeparator;
import javax.swing.JProgressBar;
import javax.swing.JSpinner;
import java.awt.Color;
import javax.swing.JFormattedTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class HomeworkUI extends JFrame {

	private JPanel contentPane;
	private JTextField ageInput;
	private JLabel ZoneTarget;
	private JTextField outputHR;
	private JComboBox<String> zoneSelect;
	private JButton btnSubmit;
	private JLabel YourMaxHr;
	private JLabel Zone;
	private JLabel MinHr;
	private JLabel MaxHr;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					HomeworkUI frame = new HomeworkUI();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public HomeworkUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 441, 329);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		ageInput = new JTextField();
		ageInput.setBounds(93, 41, 86, 20);
		contentPane.add(ageInput);
		ageInput.setColumns(10);
		
		JLabel Age = new JLabel("Age :");
		Age.setBounds(48, 41, 35, 20);
		contentPane.add(Age);
		
		ZoneTarget = new JLabel("HR Zone Target :");
		ZoneTarget.setBounds(48, 83, 86, 14);
		contentPane.add(ZoneTarget);
		
		btnSubmit = new JButton("Submit");
		btnSubmit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String HRResult = zoneSelect.getSelectedItem().toString();
				int Age = Integer.parseInt(ageInput.getText()) ;
				Calculate  hr = new  Calculate(HRResult,Age);
				outputHR.setText(""+hr.CalculateHr());
				Zone.setText(HRResult);
				MaxHr.setText("Max HR : " + hr.MaxHrZone);
				MinHr.setText("Min HR : " + hr.MinHrZone);
			}
		});
		btnSubmit.setBounds(277, 41, 91, 56);
		contentPane.add(btnSubmit);
		
	    zoneSelect = new JComboBox<String>();
	    zoneSelect.addItem("Please Select");
	    zoneSelect.addItem("MAXIMUM");
	    zoneSelect.addItem("HARD");
	    zoneSelect.addItem("MODERATE");
	    zoneSelect.addItem("LIGHT");
	    zoneSelect.addItem("VERY LIGHT");
		zoneSelect.setBounds(144, 80, 86, 20);
		contentPane.add(zoneSelect);
		
		YourMaxHr = new JLabel("Your Max HR :");
		YourMaxHr.setBounds(48, 120, 86, 20);
		contentPane.add(YourMaxHr);
		
		outputHR = new JTextField();
		outputHR.setBackground(Color.PINK);
		outputHR.setBounds(129, 120, 86, 20);
		contentPane.add(outputHR);
		outputHR.setColumns(10);
		
		JLabel HRfor = new JLabel("HR For :");
		HRfor.setBounds(48, 169, 47, 14);
		contentPane.add(HRfor);
		
		Zone = new JLabel("");
		Zone.setBounds(101, 169, 129, 14);
		contentPane.add(Zone);
		
		MinHr = new JLabel("Min HR :");
		MinHr.setBounds(48, 220, 86, 20);
		contentPane.add(MinHr);
		
		MaxHr = new JLabel("Max HR :");
		MaxHr.setBounds(144, 220, 91, 20);
		contentPane.add(MaxHr);
	}
}
