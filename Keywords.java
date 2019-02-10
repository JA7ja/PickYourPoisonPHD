package hackathon;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.TreeMap;

public class Keywords{
    private List<String> entries;
    private Map<String, Integer> keywords;
    private Map<Integer, String> sorted;
    
    public Keywords(){
	entries = new ArrayList<String>();
	keywords = new HashMap<String, Integer>();
	sorted = new TreeMap<Integer, String>();
    }

    public void setup(String fileName){
	int first = 0;
	try (Scanner sc = new Scanner(new File(fileName))){
	    while (sc.hasNextLine()){
		if (first != 0){
		    entries.add(sc.nextLine());
		}
		else{
		    first = 1;
		    sc.nextLine();
		}
	    }
	}
	catch(FileNotFoundException e){
	    System.out.println("File '" + fileName + "' not found, initializing"+
			       " both 'list' and 'array' to be empty\n");
	}
	catch(Exception e){
	    System.out.println("Error occured while extracting data:\n");
	    e.printStackTrace(); 
	}
    }

    static String[] processLine(String line){
	String proc = line;
	int tab1 = -1;
	int tab2 = -1;
	int tab3 = -1;
	for (int i = 0; i < proc.length(); i++){
	    if (proc.charAt(i) == '\t'){
		if (tab1 > 0 && tab2 > 0 && tab3 < 0)
		    tab3 = i;
		if (tab1 > 0 && tab2 < 0 && tab3 < 0 )
		    tab2 = i;
		if (tab1 < 0 && tab2 < 0 && tab3 < 0)
		    tab1 = i;
	    }
	}
	if (tab2 < 0 || tab3 < 0){
	    String[] ret = proc.split(" ");
	    return ret;
	}
	proc = proc.toLowerCase();
	proc = proc.substring(tab2, tab3);
	proc = proc.trim();
	for (int i = 0; i < proc.length(); i++){
	    if ( (proc.charAt(i) < 97) || (proc.charAt(i) > 122) ){
		if (i == 0)
		    proc = proc.substring(0, i) + proc.substring(i+1);
		else
		    proc = proc.substring(0, i) + " " + proc.substring(i+1);
	    }
	}
	return proc.split(" ");
    }

    public void process(){
	for (String e : entries){
	    String[] keys = processLine(e);
	    for (String k : keys){
		if (!keywords.containsKey(k)){
		    keywords.put(k, 1);
		}
		else{
		    keywords.put(k, keywords.get(k) + 1);
		}
	    }
	}
	sorted = new TreeMap<Integer, String>();
	for (String key : keywords.keySet()){
	    sorted.put(keywords.get(key), key);
	}
    }

    //setup, process, print
    public void printFile(){
	for(Integer key: sorted.keySet()){
            String value = sorted.get(key);
            System.out.println(key + " " + value);  
	}
	System.out.println("Finished! Size: " + keywords.size());
    }
}
