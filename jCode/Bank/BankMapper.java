import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BankMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    @Override
    protected void map(LongWritable key, Text bankRec, Context con) throws IOException, InterruptedException{
        String lines[] = bankRec.toString().split(",");
        String job = lines[1];

        int bal;
        bal = Integer.parseInt(lines[5]);
        System.out.println("Job = " + job + " Balance = " + bal);
        context.write(new Text(job), new IntWritable(bal));
    }
}