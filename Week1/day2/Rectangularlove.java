public static Rectangle findRectangularOverlap(Rectangle r1, Rectangle r2) {

        int r1_rightx=r1.getleftx()+r1.getWidth();
        int r2_rightx=r2.getleftx()+r2.getWidth();
        int r1_topy=r1.getbottomy()+r1.getHeight();
        int r2_topy=r2.getbottomy()+r2.getHeight();
        int r_leftx=Math.max(r1.getleftx(),r2.getleftx());
        int r_bottomy=Math.max(r1.getbottomy(),r2.getbottomy());
        int r_width=Math.min(r1_rightx,r2_rightx)-r_leftx;
        int r_height=Math.min(r1_topy,r2_topy)-r_bottomy;
        if(r1_topy==r2.getbottomy() || r1_rightx==r2.getleftx()) 
            return new Rectangle();
        else if(r_width<0 || r_height<0) 
            return new Rectangle();
        else 
            return new Rectangle(r_leftx,r_bottomy,r_width,r_height);

        // return new Rectangle(overlapX,overlapY,overlapWidth,overlapHeight);
    }