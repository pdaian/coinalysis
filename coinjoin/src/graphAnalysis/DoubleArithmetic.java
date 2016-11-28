package graphAnalysis;

import java.math.BigDecimal;    

public class DoubleArithmetic {    
  
    private static final int DEF_DIV_SCALE = 10;    
           
    private DoubleArithmetic(){    
    }    
  
    public static double add(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(Double.toString(v1));    
        BigDecimal b2 = new BigDecimal(Double.toString(v2));    
        return b1.add(b2).doubleValue();    
    }    
       
    public static double sub(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(Double.toString(v1));    
        BigDecimal b2 = new BigDecimal(Double.toString(v2));    
        return b1.subtract(b2).doubleValue();    
    }    
       
    public static double mul(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(Double.toString(v1));    
        BigDecimal b2 = new BigDecimal(Double.toString(v2));    
        return b1.multiply(b2).doubleValue();    
    }    
  
    public static double div(double v1,double v2){    
        return div(v1,v2,DEF_DIV_SCALE);    
    }    
  
    public static double div(double v1,double v2,int scale){    
        if(scale<0){    
            throw new IllegalArgumentException(    
                "The scale must be a positive integer or zero");    
        }    
        BigDecimal b1 = new BigDecimal(Double.toString(v1));    
        BigDecimal b2 = new BigDecimal(Double.toString(v2));    
        return b1.divide(b2,scale,BigDecimal.ROUND_HALF_UP).doubleValue();    
    }    
  
    public static double round(double v,int scale){    
        if(scale<0){    
            throw new IllegalArgumentException(    
                "The scale must be a positive integer or zero");    
        }    
        BigDecimal b = new BigDecimal(Double.toString(v));    
        BigDecimal one = new BigDecimal("1");    
        return b.divide(one,scale,BigDecimal.ROUND_HALF_UP).doubleValue();    
    }    
       
    public static float convertsToFloat(double v){    
        BigDecimal b = new BigDecimal(v);    
        return b.floatValue();    
    }    
       
    public static int convertsToInt(double v){    
        BigDecimal b = new BigDecimal(v);    
        return b.intValue();    
    }    
  
    public static long convertsToLong(double v){    
        BigDecimal b = new BigDecimal(v);    
        return b.longValue();    
    }    
  
    public static double returnMax(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(v1);    
        BigDecimal b2 = new BigDecimal(v2);    
        return b1.max(b2).doubleValue();    
    }    
  
    public static double returnMin(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(v1);    
        BigDecimal b2 = new BigDecimal(v2);    
        return b1.min(b2).doubleValue();    
    }    
  
    public static int compareTo(double v1,double v2){    
        BigDecimal b1 = new BigDecimal(v1);    
        BigDecimal b2 = new BigDecimal(v2);    
        return b1.compareTo(b2);    
    }   
  
}  
