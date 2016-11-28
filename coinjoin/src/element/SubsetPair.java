package element;

import graphAnalysis.DoubleArithmetic;

public class SubsetPair {
	public Subset inputSubset, outputSubset;
	public double subCost;
	
	public SubsetPair(Subset in, Subset out){
		this.inputSubset = in;
		this.outputSubset = out;
		subCost = DoubleArithmetic.sub(in.sum, out.sum);
	}
	
	public boolean isValid(){
		return subCost >= 0;
	}
}
