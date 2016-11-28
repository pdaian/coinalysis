package element;

import java.util.Comparator;

public class Subset {
	public byte[] indicator;
	public double sum;
	private int totalSize;
	public int type;
	
	public Subset(byte[] indicator, double sum, int type){
		this.indicator = indicator;
		this.sum = sum; 
		if (indicator != null) totalSize = indicator.length;
		this.type = type;
	}
	
	public void print(){
		System.out.print("\tIndicator: [");
		for (int i = 0; i < totalSize - 1; i++)
			System.out.print(indicator[i] + " ");
		System.out.println(indicator[totalSize - 1] + "]");
		System.out.println("\tSum: " + sum);
	}
	
	public static class SubsetComparator implements Comparator<Subset>{

		@Override
		public int compare(Subset s1, Subset s2) {
			if (s1.sum < s2.sum) return -1;
			if (s1.sum > s2.sum) return 1;
			return 0;
		}
		
	}
}
