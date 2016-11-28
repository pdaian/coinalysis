package element;

import java.util.ArrayList;
import java.util.List;

import graphAnalysis.DoubleArithmetic;

public class Transaction {
	//private double[] input, output;
	public List<Node> input, output;
	public double inSum, outSum, cost; // Sum of input value, sum of output value, cost of transaction
	
	public Transaction(){
		input = new ArrayList<Node>();
		output = new ArrayList<Node>();
		cost = 0;
	}
	
	public void addInput(Node node){
		this.input.add(node);
	//	inSum += node.getValue();
	//	cost += node.getValue();
		inSum = DoubleArithmetic.add(inSum, node.value);
		cost = DoubleArithmetic.add(cost, node.value);
	}
	
	public void addOutput(Node node){
		this.output.add(node);
	//	outSum += node.getValue();
	//	cost -= node.getValue();
		outSum = DoubleArithmetic.add(outSum, node.value);
		cost = DoubleArithmetic.sub(cost, node.value);
	}
	
	public void removeInput(int i){
	//	inSum -= input.get(i).getValue();
		inSum = DoubleArithmetic.sub(inSum, input.get(i).value);
	//	cost = cost - input.get(i).getValue();
		cost = DoubleArithmetic.sub(cost, input.get(i).value);
		input.remove(i);
	}
	
	public void print(){
		System.out.println("InputSum: " + inSum + "\tOutputSum: " + outSum + "\tCost: " + cost);
		System.out.println("\nInput \t\t\tOutput\n");
		int i = 0;
		for (; i < input.size(); i++){
			System.out.print(input.get(i).getName() + "\t" + input.get(i).getValue());
			if (i < output.size())
				System.out.print("\t\t" + output.get(i).getName() + "\t" + output.get(i).getValue());
			System.out.println();
		}
		for (; i < output.size(); i++)
			System.out.println("\t\t\t" + output.get(i).getName() + "\t" + output.get(i).getValue());
	}
}
