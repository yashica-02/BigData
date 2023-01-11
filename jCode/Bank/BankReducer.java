import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class FirstMapReduceReducer extends Reducer<Text, IntWritable, Text, Text> {
    @Override
    protected void reduce(Text key, Iterable<IntWritable> valueList, Context con) throws IOException, InterruptedException{
    try{
        Integer total = (int) 0;
        int count =0;
        for(IntWritable var : valueList){
        total += var.get();
        System.out.println("key: " + key + " value: " + var.get());
        count++;
        }

        Integer avg = (Integer) total/count;
        String out = "Total: " + total + " ::  "+ "Average: " + avg;
        con.write(key, new Text(out));
        }

    }
    
    catch (Exception e){}
    }
}