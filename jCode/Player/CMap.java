import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CMap extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text Rec, Context con) throws IOException, InterruptedException {
        String lines [] = Rec.toString().split(",");
        int flag = 1;

        //Ignore header line
        if (lines [0].equals ("Innings Player"))
            flag =0;

        if (flag == 1){
            String playerName = lines [0];
            int score = 0;

            //only consider records where score has an integer value
            try{
                score = Integer.parseInt(lines[2]);
            }
            catch (NumberFormatException e){
                flag =0;
            }

            if(flag==1){
                System.out,println("Player: " + playerName + "Score: "+ score);
                con.write(new Text(playerName), new IntWritable(score));
            }
        }
    }
}