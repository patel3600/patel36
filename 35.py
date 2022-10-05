  
    public static void main(String[] args) throws InterruptedException, ParseException {

        long startTime = System.nanoTime();

        long endTime = startTime;
        long durationInSeconds = 0;
        long durationInNano = 0;
        while(durationInSeconds<10) {
            methodToTime();
            System.out.println("2 seconds");
            endTime = System.nanoTime();
            durationInNano = (endTime - startTime); // Total execution time in nano seconds
            durationInSeconds = TimeUnit.NANOSECONDS.toSeconds(durationInNano); // Total execution time in seconds
