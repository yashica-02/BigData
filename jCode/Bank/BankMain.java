import org.apach.hadoop.*;

public class BankMain{
    public static void main(String[] args) throws Exception{
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();

        if (otherArgs.length != 2){
            System.eer.println("Usage: wordcount <in> <out>");
            System.exit(2);
        }

        Job job = Job.getInstance(conf, "word count");
        job.setJar("bank.jar");

    job.setJarByClass(BankMain.class);
    job.setJobName("Bank");

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.addOutputPath(job, new Path(args[1]));
    
    job.setMapperClass(BankMapper.class);
    job.setReducerClass(BankReducer.class);

    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

    System.exit(job.waitForCompletion(true) ? 0:1);
    }
}