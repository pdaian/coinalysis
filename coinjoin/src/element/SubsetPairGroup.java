package element;

import java.util.ArrayList;
import java.util.List;

import graphAnalysis.DoubleArithmetic;

public class SubsetPairGroup {
	public List<SubsetPair> pairs;
	public byte[] inputInd, outputInd;
	public double groupCost;
	private int inputSize, outputSize;
	private boolean valid = true;
	
	public SubsetPairGroup(SubsetPair pair){
		this(pair.inputSubset.indicator.length, pair.outputSubset.indicator.length);
		
		pairs.add(pair);
		for (int i = 0; i < inputSize; i++) inputInd[i] = pair.inputSubset.indicator[i];
		for (int i = 0; i < outputSize; i++) outputInd[i] = pair.outputSubset.indicator[i];
		groupCost = pair.subCost;
	}
	
	public SubsetPairGroup(int inputSize, int outputSize){
		this.pairs = new ArrayList<SubsetPair>();
		this.inputSize = inputSize;
		this.outputSize = outputSize;
		inputInd = new byte[inputSize];
		outputInd = new byte[outputSize];	
	}
	
	public SubsetPairGroup(SubsetPairGroup g){
		this.pairs = new ArrayList<SubsetPair>();
		for (int i = 0; i < g.pairs.size(); i++) this.pairs.add(g.pairs.get(i));
		this.inputSize = g.inputSize;
		this.outputSize = g.outputSize;
	//	inputInd = new byte[inputSize];
		inputInd = g.inputInd.clone();
	//	outputInd = new byte[outputSize];	
		outputInd = g.outputInd.clone();
	}
	
	/*
	 * Test if the pair can be added into this group, if yes, add it; if not
	 */
	public void tryToAdd(SubsetPair pair){
//		for (int i = 0; i < inputSize; i++) if (inputInd[i] == 1 && pair.inputSubset.indicator[i] == 1) return false;
//		for (int i = 0; i < outputSize; i++) if (outputInd[i] == 1 && pair.outputSubset.indicator[i] == 1) return false;
//		pairs.add(pair);
//		for (int i = 0; i < inputSize; i++) if (pair.inputSubset.indicator[i] == 1) inputInd[i] = 1;
//		for (int i = 0; i < outputSize; i++) if (pair.outputSubset.indicator[i] == 1) outputInd[i] = 1;
//		groupCost = DoubleArithmetic.add(groupCost, pair.subCost);
//		return true;
		
		pairs.add(pair);
		for (int i = 0; i < inputSize; i++){
			if (pair.inputSubset.indicator[i] == 1){
				if (inputInd[i] == 1) valid = false;
				inputInd[i] = 1;
			}
		}
		for (int i = 0; i < outputSize; i++){
			if (pair.outputSubset.indicator[i] == 1){
				if (outputInd[i] == 1) valid = false;
				outputInd[i] = 1;
			}
		}
		groupCost = DoubleArithmetic.add(groupCost, pair.subCost);
	}
	
	public boolean isFinished(){
	//	System.out.print("inputInd: "); for (int i = 0; i < inputSize; i++) System.out.print(inputInd[i] + " "); System.out.println();
		for (int i = 0; i < inputSize; i++) if (inputInd[i] == 0) return false;
		for (int i = 0; i < outputSize; i++) if (outputInd[i] == 0) return false;
		return valid;
	}
	
	public void print(){
		SubsetPair pair;
		for (int i = 0; i < pairs.size(); i++){
			System.out.println("Pair " + i + ": ");
			pair = pairs.get(i);
			System.out.print("\tInputSubset:");
			for (int j = 0; j < inputSize; j++){
				System.out.print(pair.inputSubset.indicator[j] + " ");
			}
			System.out.println();
			System.out.print("\tOutputSubset:");
			for (int j = 0; j < outputSize; j++){
				System.out.print(pair.outputSubset.indicator[j] + " ");
			}
			System.out.println();
		}
	}
}
