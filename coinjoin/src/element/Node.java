package element;

public class Node {
	
	public String name; // identify address
	public double value;
	public int type;
	
	public Node(String name, double value){
		this.name = name;
		this.value = value;
	}
	
	public void setName(String name){
		this.name = name;
	}
	
	public void setValue(double value){
		this.value = value;
	}
	
	public String getName(){
		return this.name;
	}
	
	public double getValue(){
		return this.value;
	}
}
