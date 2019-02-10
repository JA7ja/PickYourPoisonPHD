package hackathon;

public class KeywordsDriver{
    public static void main(String[] args){
	Keywords keywordsExtractor = new Keywords();
	keywordsExtractor.setup("keywords_text.txt");
	keywordsExtractor.process();
	keywordsExtractor.printFile();
    }
}
