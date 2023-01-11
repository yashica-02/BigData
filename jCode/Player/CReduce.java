import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CReduce extends Reducer <Text, IntWritable, Text, Text>{
    @Override
    public void reduce(Text key, Iterable<IntWritable> valueList, Context con) throws IOException, InterruptedException {
        try{
            Integer total = (int) 0;
            Integer max = (int) 0;
            int count =0;

            for (IntWritable var: valueList){
                total += var.get();
                count++;

                if (var.get() > max)
                    max = var.get();
            }

            float avg = (float) total/count;

            String out = "Total: " + total + " :: " + "Average: " + avg + " :: " + "Max: " + max;
            con.write(key, new Text(out));
        }
        catch (Exception e){}
    }
}