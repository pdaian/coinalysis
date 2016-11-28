package graphAnalysis;


import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import element.*;

public class TransactionAnalysis {
	public final static int INPUT = 1, OUTPUT = 2;
	
	public static void main(String[] args){
		/* Test functions */
		Transaction tx = initializeGraphNodes(args[0]);
		joinAndCounteract(tx);
		ignoreSmallInput(tx);
		//if (!isValidTransaction) 
		List<Subset> inputSubsets = calculateSubsets(tx.input, INPUT);
		List<Subset> outputSubsets = calculateSubsets(tx.output, OUTPUT);
		if (inputSubsets.size() == 0 || outputSubsets.size() == 0){ // at least one of list has only one node, cannot be further partitioned
			System.out.println("At least one side has only one party");
			System.out.println("#Different partitions: 0");
			return;
		}
		List<SubsetPair> pairList = calculateValidSubsetPairs(inputSubsets, outputSubsets, tx.cost);
		if (pairList.size() == 0){ // No valid pairs formed
			System.out.println("No valid pairs formed");
			System.out.println("#Different partitions: 0");
			return;
		}
		List<SubsetPairGroup> groupList = calculateCoveringSubsetPairGroups(pairList);
		System.out.println("#Different Paritions: " + groupList.size());
	}
	
	/*
	 * Read addresses and values from file
	 * Return bipartite with origin nodes and no edges
	 */
	private static Transaction initializeGraphNodes(String filePath){
		Transaction tx = new Transaction();
		String currLine;
		int type = -1;
		try {
			Scanner scanner = new Scanner(new FileInputStream(filePath));
			while (scanner.hasNext()){
				currLine = scanner.nextLine();
				if (currLine.length() > 0 && currLine.charAt(0) == '#'){
					if (currLine.contains("input")) type = INPUT;
					else if (currLine.contains("output")) type = OUTPUT;
					continue;
				}
				if (currLine.length() == 0) continue;
				String[] s = currLine.split(" ");
				if (type == INPUT) tx.addInput(new Node(s[0], Double.parseDouble(s[1])));
				else if (type == OUTPUT) tx.addOutput(new Node(s[0], Double.parseDouble(s[1])));
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	//	System.out.println("\n======== After read in ========");
	//	tx.print();
		if (tx.cost >= 0) return tx;
		else{
			System.out.println("Error: negative fee");
			System.exit(0);
			return null;
		}
	}
	
	/*
	 * Determine if input transaction is a valid transaction
	 */
	private static boolean isValidTransaction(Transaction trans){
		return trans.cost >= 0;
	}
	
	/*
	 * Join the same address in input nodes
	 * Reduce the same node from both input and output nodes
	 */
	private static void joinAndCounteract(Transaction trans){
		List<Node> inputNodes = trans.input, outputNodes = trans.output;
		Map<String, Double> inMap = new HashMap<String, Double>();
		Map<String, Double> outMap = new HashMap<String, Double>();
		ArrayList<String> overlap = new ArrayList<String>();
		Node curr;
		// add input address-value tuple into map
		for (int i = 0; i < inputNodes.size(); i++){
			curr = inputNodes.get(i);
			if (inMap.get(curr.getName()) == null)
				inMap.put(curr.getName(), curr.getValue());
			else 
			//	inMap.put(curr.getName(), inMap.get(curr.getName()) + curr.getValue());
				inMap.put(curr.getName(), DoubleArithmetic.add(inMap.get(curr.getName()), curr.getValue()));
		}
		// add output address-value tuple into map
		// determine if there are same addresses in input and output group
		for (int i = 0; i < outputNodes.size(); i++){
			curr = outputNodes.get(i);
			if (outMap.get(curr.getName()) == null)
				outMap.put(curr.getName(), curr.getValue());
			else 
			//	outMap.put(curr.getName(), outMap.get(curr.getName()) + curr.getValue());
				outMap.put(curr.getName(), DoubleArithmetic.add(outMap.get(curr.getName()), curr.getValue()));
			// if this address appears both in input and output
			if (inMap.get(curr.getName()) != null && !overlap.contains(curr.getName()))
				overlap.add(curr.getName());
		}
		
		// delete overlap addresses from one group
		String name;
		double inputv, outputv;
		for (int i = 0; i < overlap.size(); i++){
			name = overlap.get(i);
			inputv = inMap.get(name);
			outputv = outMap.get(name);
			if (inputv > outputv){
			//	inMap.put(name, inputv - outputv);
				inMap.put(name, DoubleArithmetic.sub(inputv, outputv));
				outMap.remove(name);
			}
			else if (inputv < outputv){
				inMap.remove(name);
			//	outMap.put(name, outputv - inputv);
				outMap.put(name, DoubleArithmetic.sub(outputv, inputv));
			}
			else {
				inMap.remove(name);
				outMap.remove(name);
			}
		}
		
		// construct new input and output list
		inputNodes = new ArrayList<Node>();
		outputNodes = new ArrayList<Node>();
		Iterator<String> inputName = inMap.keySet().iterator();
		Iterator<String> outputName = outMap.keySet().iterator();
		double inSum = 0, outSum = 0;
		while (inputName.hasNext()){
			name = inputName.next();
			inputNodes.add(new Node(name, inMap.get(name)));
		//	inSum += inMap.get(name);
			inSum = DoubleArithmetic.add(inSum, inMap.get(name));
		}
		while (outputName.hasNext()){
			name = outputName.next();
			outputNodes.add(new Node(name, outMap.get(name)));
		//	outSum += outMap.get(name);
			outSum = DoubleArithmetic.add(outSum, outMap.get(name));
		}
//		trans.setinput(inputNodes);
//		trans.setOutput(outputNodes);
//		trans.setInsum(inSum);
//		trans.setOutsum(outSum);
//		trans.setCost(inSum - outSum);
		trans.input = inputNodes;
		trans.output = outputNodes;
		trans.inSum = inSum;
		trans.outSum = outSum;
	//	trans.cost = inSum - outSum;
		trans.cost = DoubleArithmetic.sub(inSum, outSum);
		
	//	System.out.println("\n======== After join and counteract ========");
	//	trans.print();
	}
	
	/*
	 * Ignore input node with amount less than cost
	 * Reduce these amount from total cost
	 */
	private static void ignoreSmallInput(Transaction trans){
//		ArrayList<Node> inputNodes = trans.getInput();
//		for (int i = 0; i < inputNodes.size(); i++){
//			if (inputNodes.get(i).getValue() < trans.getCost())
//				trans.removeInput(i);
//		}
		List<Node> inputNodes = trans.input;
		for (int i = 0; i < inputNodes.size(); i++){
			if (inputNodes.get(i).getValue() < trans.cost){
				trans.removeInput(i);
				i--;
			}	
		}
		
	//	System.out.println("\n======== After ignore small inputs ========");
	//	trans.print();
	}
	
	/*
	 * Calculate sum of every non-empty subset of input list and output list 
	 */
	private static List<Subset> calculateSubsets(List<Node> nodeList, int type){
		List<Subset> subsetList = new ArrayList<Subset>();
		int l = nodeList.size();
		
		// if the list is empty, P(L) is empty
		if (l == 0) return subsetList;
		// if the list is non-empty
		Node currNode = nodeList.get(0);
		byte[] currIndicator, nextInd0 = new byte[l], nextInd1 = new byte[l];
		nextInd0[0] = 0; nextInd1[0] = 1;
		subsetList.add(new Subset(nextInd0, 0, type));
		subsetList.add(new Subset(nextInd1, currNode.value, type));
		int length = 2;
		Subset cSub;
		for (int i = 1; i < l; i++){
			// For l-th level of the tree
			currNode = nodeList.get(i);
			// remove "length" elements from list
			// add 2 * length elements into list
			// or just update and insert
			for (int j = 0; j < length; j++){
				cSub = subsetList.get(j * 2);
				nextInd0 = cSub.indicator;
				nextInd1 = new byte[l];
				for (int k = 0; k < i; k++) nextInd1[k] = nextInd0[k]; // copy the indicator
				nextInd0[i] = 0; nextInd1[i] = 1; // determine next indicator
				subsetList.add(
						2 * j + 1,
						new Subset(nextInd1, DoubleArithmetic.add(cSub.sum, currNode.value), type));
			}
			length *= 2;
		}
		
		subsetList.remove(subsetList.size() - 1); // remove the whole set
		subsetList.remove(0); // remove the empty set
		
	//	System.out.println("#subsets: " + subsetList.size());
		
		return subsetList;
	}
	
	
	/*
	 * Sort all 2^n + 2^m input and output subsets
	 * Find all valid (i.e. 0 <= cost <= c) pairs of input subset and output subset
	 * Form a list of valid SubsetPair
	 */
	private static List<SubsetPair> calculateValidSubsetPairs(List<Subset> inputSubsets, List<Subset> outputSubsets, double c){
		List<SubsetPair> pairList = new ArrayList<SubsetPair>();
		
		List<Subset> merged = new ArrayList<Subset>();
		merged.addAll(inputSubsets);
		merged.addAll(outputSubsets);
		merged.sort(new Subset.SubsetComparator()); // Sort all subset by ascending order
	//	 for (int i = 0; i < merged.size(); i++) System.out.print(merged.get(i).sum + " "); System.out.println();
		
		int inputSubsetNum = inputSubsets.size();
		int outputSubsetNum = outputSubsets.size();
		int totalNum = inputSubsetNum + outputSubsetNum;
		int index;
		Subset currInputSubset;
		for (int i = 0; i < inputSubsetNum; i++){
			currInputSubset = inputSubsets.get(i); //currInputSubset.print();
			index = merged.indexOf(currInputSubset); //System.out.println(index);
			for (int j = index - 1; j >= 0; j--){
				if (merged.get(j).sum >= DoubleArithmetic.sub(currInputSubset.sum, c)){
					if (merged.get(j).type == OUTPUT) pairList.add(new SubsetPair(currInputSubset, merged.get(j)));
					else continue;
				}
				else break;
			}
			for (int j = index + 1; j < totalNum; j++){
				if (merged.get(j).sum > currInputSubset.sum) break;
				else if (merged.get(j).type == OUTPUT) pairList.add(new SubsetPair(currInputSubset, merged.get(j)));
			}
		}
		
	//	System.out.println("#valid pairs of subset: " + pairList.size());
		return pairList;
	}
	
	/*
	 * Calculate all successful group of pairs, 
	 * which covers the whole set, and each pair is a valid pair
	 * => Final result
	 */
	private static List<SubsetPairGroup> calculateCoveringSubsetPairGroups(List<SubsetPair> pairList){
		List<SubsetPairGroup> groupList = new ArrayList<SubsetPairGroup>();
		SubsetPairGroup group;
		
		int inputSize = pairList.get(0).inputSubset.indicator.length;
		int outputSize = pairList.get(0).outputSubset.indicator.length;
		groupList.add(new SubsetPairGroup(inputSize, outputSize));
		groupList.add(new SubsetPairGroup(pairList.get(0)));
		int length = 2;
		SubsetPair currPair;
		for (int i = 1; i < pairList.size(); i++){
			currPair = pairList.get(i);
			for (int j = 0; j < length; j++){
				group = new SubsetPairGroup(groupList.get(2 * j));
				group.tryToAdd(currPair);
				groupList.add(2 * j + 1, group);
			}
			length *= 2;
		}
	//	System.out.println(groupList.size());
		
		for (int i = 0; i < groupList.size(); i++){
			if (!groupList.get(i).isFinished()){
				groupList.remove(i);
				i--;
			}
		}
		
	//	for (int i = 0; i < groupList.size(); i++)
	//		groupList.get(i).print();
		
		
		return groupList;
	}
}
