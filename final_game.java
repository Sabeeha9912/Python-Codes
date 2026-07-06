import javax.sound.sampled.*;
import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;   //Abstract Window Toolkit
import java.util.Random;
import java.util.*;

public class final_game extends JFrame { //JFrame is a class comes from swings
    private char character;
    static class SoundModule {
        public static void playNoise(int ms, double vol) {
            try {
                float r = 8000f;
                byte[] b = new byte[(int)(r * (ms / 1000f))];
                Random rand = new Random();
                for (int i = 0; i < b.length; i++)
                    b[i] = (byte)((rand.nextFloat() * 2.0 - 1.0) * 127.0 * vol);
                SourceDataLine l = AudioSystem.getSourceDataLine(new AudioFormat(r, 8, 1, true, false));
                l.open();
                l.start();
                l.write(b, 0, b.length);
                l.drain();
                l.close();
            }
            catch (Exception e) {}
        }
        public static void playTone(int f, int ms, double v) {
            try {
                float r = 8000f; byte[] b = new byte[(int)(r * (ms / 1000f))];
                for (int i = 0; i < b.length; i++) b[i] = (byte)(Math.sin(i / (r / f) * 2.0 * Math.PI) * 127.0 * v);
                SourceDataLine l = AudioSystem.getSourceDataLine(new AudioFormat(r, 8, 1, true, true));
                l.open();
                l.start();
                l.write(b, 0, b.length);
                l.drain();
                l.close();
            } catch (Exception e) {}
        }
        //correct guess sound
        public static void playCorrect() {
            new Thread(() -> {
                playTone(523, 80, 0.4); playTone(659, 120, 0.4); }).start(); }
        public static void playWrong()   { new Thread(() -> playNoise(200, 0.5)).start(); }
        public static void playWarning() { new Thread(() -> playTone(880, 60, 0.4)).start(); }
        public static void playGameOver(boolean win) {
            new Thread(() -> {
                if (win) {
                    for(int x : new int[]{523,659,784,1046}) playTone(x,100,0.4); }
                else { for(int x : new int[]{180,130,90}) playTone(x,250,0.6); }
            }).start();
        }
    }
    static class WordManager {
        private final String word, description; private final char[] display;
        private static final String[][] LIST = {
                {"java","programming language"},{"code","software developer tool"},{"play","have fun or replicate a game"},
                {"desk","office furniture item"},{"book","something you read"},{"apple","crisp round fruit"},
                {"beach","sandy ocean shore"},{"castle","fortified medieval building"},{"elixir","magical healing potion"},{"cat","domestic animal"}
        };

        public WordManager() {           //constructer
            int idx = new Random().nextInt(LIST.length); word = LIST[idx][0]; description = LIST[idx][1];
            Arrays.fill(display = new char[word.length()], '_');
        }
        public String getWord() { return word; }
        public String getDescription() { return description; }
        public boolean reveal(char c) {
            boolean f = false; for (int i=0; i<word.length(); i++) if (word.charAt(i)==c) { display[i]=c; f=true; } return f;
        }
        public String getDisplay() {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < display.length; i++) sb.append(display[i]).append(i < display.length - 1 ? " " : "");
            return sb.toString();
        }
        public boolean isComplete() { for (char c : display) if (c == '_') return false; return true; }
    }
    static class GameLogic {
        private WordManager wm; int warnings, guessesLeft, wrong, totalGuessesUsed;
        Set<Character> guessed = new HashSet<>(), avail = new LinkedHashSet<>();
        public GameLogic() { newGame(); }
        public void newGame() {
            wm = new WordManager(); warnings = 4; guessesLeft = (int)Math.ceil(wm.getWord().length()*1.5); wrong = totalGuessesUsed = 0;
            guessed.clear(); avail.clear(); for(char c='a'; c<='z'; c++) avail.add(c);
        }
        public WordManager getWm() { return wm; }
        public enum Res { CORRECT, INCORRECT, ALREADY, INVALID, WIN, LOSE }
        public Res process(char c) {
            if (!Character.isLetter(c) || guessed.contains(c)) return pen();
            guessed.add(c); avail.remove(c); totalGuessesUsed++;
            boolean found = wm.reveal(c); if (!found) wrong++; guessesLeft--;
            if (wm.isComplete()) return Res.WIN;
            return (guessesLeft <= 0 || wrong >= 6) ? Res.LOSE : (found ? Res.CORRECT : Res.INCORRECT);
        }
        private Res pen() {
            if (warnings > 0) warnings--; else guessesLeft--;
            return (guessesLeft <= 0 || wrong >= 6) ? Res.LOSE : Res.INVALID;
        }
    }

    static class HangmanPanel extends JPanel {   // JPanel p = new HangmanPanel(); it will b polymorphism
        private int linesToDraw = 0, textLabelValue = 0;
        public HangmanPanel() { setBackground(new Color(12,18,40)); setPreferredSize(new Dimension(240,280)); }
        public void setData(int t, int w) { textLabelValue = t; linesToDraw = w; repaint(); }
        // JPanel method overrides
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            //downcasting (when swing calls paintComponent(Graphics g) it will give Graphics g) but obj is gr.2d
            //Converting a parent-class reference back into a child-class reference
            Graphics2D g2 = (Graphics2D)g;
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setStroke(new BasicStroke(5f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));
            g2.setColor(new Color(160,140,80)); g2.drawPolyline(new int[]{25,160,70,70,160,160}, new int[]{260,260,260,30,30,60}, 6);
            int cx = 160; g2.setStroke(new BasicStroke(3f));
            if (linesToDraw >= 1) { g2.setColor(new Color(255,200,120)); g2.drawOval(cx-18,60,36,36); }
            if (linesToDraw >= 2) { g2.setColor(new Color(100,180,255)); g2.drawLine(cx,96,cx,170); }
            if (linesToDraw >= 3) g2.drawLine(cx,115,cx-30,145); if (linesToDraw >= 4) g2.drawLine(cx,115,cx+30,145);
            if (linesToDraw >= 5) g2.drawLine(cx,170,cx-25,215); if (linesToDraw >= 6) g2.drawLine(cx,170,cx+25,215);
            g2.setColor(new Color(230,70,70,180)); g2.fillRoundRect(8,8,55,24,8,8);
            g2.setColor(Color.WHITE); g2.setFont(new Font("Arial", Font.BOLD, 11)); g2.drawString(" x"+textLabelValue+"/6",14,24);
        }
    }
    private final GameLogic game = new GameLogic(); private HangmanPanel hp;
    private JLabel wordL, msgL, guessL, warnL, availL, descL; private JTextField input;
    private JButton submitB, resetB; private JButton[] letterBtns = new JButton[26];
    private CardLayout mainLayout = new CardLayout(); private JPanel cardContainer;

    public final_game() {
        setTitle("Hangman Game"); setDefaultCloseOperation(EXIT_ON_CLOSE); setResizable(false);
        cardContainer = new JPanel(mainLayout); JPanel gamePanel = new JPanel(new BorderLayout()); gamePanel.setBackground(new Color(10,15,35));
        JPanel top = new JPanel(new GridLayout(2,1)); top.setBackground(new Color(14,22,52)); top.setBorder(new EmptyBorder(10,10,10,10));
        JLabel title = new JLabel("⚓ HANGMAN", 0); title.setFont(new Font("Arial", 1, 26)); title.setForeground(new Color(255,200,50));
        JLabel sub = new JLabel("Computer Engineering Department", 0); sub.setForeground(new Color(140,150,195));
        top.add(title); top.add(sub); gamePanel.add(top, BorderLayout.NORTH);
        JPanel ctr = new JPanel(new BorderLayout(15,0)); ctr.setOpaque(false); ctr.setBorder(new EmptyBorder(10,15,10,15));
        hp = new HangmanPanel(); hp.setBorder(BorderFactory.createLineBorder(new Color(40,60,120),2)); ctr.add(hp, BorderLayout.WEST);
        JPanel right = new JPanel(); right.setLayout(new BoxLayout(right, BoxLayout.Y_AXIS)); right.setOpaque(false);
        JPanel stats = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 0)); stats.setOpaque(false);
        stats.add(guessL = makeLabel()); stats.add(warnL = makeLabel()); right.add(stats); right.add(Box.createVerticalStrut(15));
        descL = new JLabel("", 0); descL.setFont(new Font("Arial", Font.ITALIC, 14)); descL.setForeground(new Color(200, 200, 200)); descL.setAlignmentX(0.5f); right.add(descL); right.add(Box.createVerticalStrut(15));
        wordL = new JLabel("", 0); wordL.setFont(new Font("Courier New", 1, 32)); wordL.setForeground(Color.WHITE); wordL.setAlignmentX(0.5f); right.add(wordL); right.add(Box.createVerticalStrut(20));
        msgL = new JLabel("Type or click a letter!", 0); msgL.setFont(new Font("Arial", 1, 13)); msgL.setForeground(new Color(100,180,255)); msgL.setAlignmentX(0.5f); right.add(msgL); right.add(Box.createVerticalStrut(15));
        availL = new JLabel("", 0); availL.setFont(new Font("Courier New", Font.BOLD, 14)); availL.setForeground(new Color(170,190,255)); availL.setAlignmentX(0.5f); right.add(availL);
        ctr.add(right, BorderLayout.CENTER); gamePanel.add(ctr, BorderLayout.CENTER);
        JPanel btm = new JPanel(); btm.setLayout(new BoxLayout(btm, BoxLayout.Y_AXIS)); btm.setBackground(new Color(14,20,44)); btm.setBorder(new EmptyBorder(10,10,10,10));
        JPanel kb = new JPanel(new FlowLayout(FlowLayout.CENTER,3,3)); kb.setOpaque(false);
        for(int i=0; i<26; i++) {
            char c = (char)('a'+i); letterBtns[i] = new JButton(String.valueOf(c).toUpperCase());
            letterBtns[i].setFont(new Font("Arial", Font.BOLD, 11)); letterBtns[i].setBackground(new Color(28,48,105)); letterBtns[i].setForeground(Color.WHITE);
            letterBtns[i].setPreferredSize(new Dimension(48, 34)); letterBtns[i].addActionListener(e -> action(String.valueOf(c))); kb.add(letterBtns[i]);
        }
        btm.add(kb); JPanel btmCtrl = new JPanel(new FlowLayout(1,10,5)); btmCtrl.setOpaque(false);
        JLabel inputPrompt = new JLabel("Guess:"); inputPrompt.setForeground(Color.WHITE); btmCtrl.add(inputPrompt);
        input = new JTextField(4); input.setHorizontalAlignment(0); input.addActionListener(e -> sendInput()); btmCtrl.add(input);
        submitB = new JButton("Go"); submitB.addActionListener(e -> sendInput()); btmCtrl.add(submitB);
        resetB = new JButton("Reset"); resetB.setBackground(new Color(165,55,55)); resetB.setForeground(Color.WHITE); resetB.addActionListener(e -> reset()); btmCtrl.add(resetB);
        btm.add(btmCtrl); gamePanel.add(btm, BorderLayout.SOUTH); cardContainer.add(gamePanel, "GAME"); add(cardContainer);
        pack(); setMinimumSize(new Dimension(1220, 580)); setLocationRelativeTo(null); update("");
    }
    private JLabel makeLabel() {
        JLabel l = new JLabel("", 0); l.setFont(new Font("Arial", Font.BOLD, 11)); l.setOpaque(true); l.setBackground(new Color(20,30,60));
        l.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createLineBorder(new Color(50,70,130)), new EmptyBorder(3,8,3,8))); return l;
    }
    private void sendInput() { String s = input.getText(); input.setText(""); if(!s.isEmpty()) action(s); }
    private void action(String s) {
        String t = s.trim().toLowerCase(); boolean isSymbolOrDigit = false;
        for (char ch : t.toCharArray()) { if (!Character.isLetter(ch)) { isSymbolOrDigit = true; break; } }
        if (t.isEmpty()) t = " "; this.character = t.charAt(0);
        if (Character.isLetter(this.character)) letterBtns[this.character - 'a'].setEnabled(false);
        GameLogic.Res r = game.process(this.character); String letterUpper = String.valueOf(this.character).toUpperCase();
        if (r == GameLogic.Res.CORRECT)   { update("Good job! '" + letterUpper + "' is inside."); SoundModule.playCorrect(); }
        if (r == GameLogic.Res.INCORRECT) { update("Oops! '" + letterUpper + "' is wrong."); SoundModule.playWrong(); }
        if (r == GameLogic.Res.ALREADY)   { update("You already guessed '" + letterUpper + "'."); SoundModule.playWarning(); }
        if (r == GameLogic.Res.INVALID)   { update(isSymbolOrDigit ? "Invalid entry. Digits and special symbols are not allowed!" : "Invalid entry. Use single A-Z letters."); SoundModule.playWarning(); }
        if (r == GameLogic.Res.WIN || r == GameLogic.Res.LOSE) {
            boolean w = (r == GameLogic.Res.WIN); update(w ? " Victory!" : " Game Over!"); SoundModule.playGameOver(w);
            hp.paintImmediately(0, 0, hp.getWidth(), hp.getHeight());
            javax.swing.Timer delayTransition = new javax.swing.Timer(500, e -> triggerFullBlackScreen(w)); delayTransition.setRepeats(false); delayTransition.start();
        }
    }
    private void reset() {
        game.newGame(); for(JButton b : letterBtns) b.setEnabled(true); input.setEnabled(true); submitB.setEnabled(true);
        update("Game reset!"); mainLayout.show(cardContainer, "GAME");
    }
    private void update(String msg) {
        wordL.setText("<html><center>" + game.getWm().getDisplay().toUpperCase() + "</center></html>");
        descL.setText("<html><center>Hint: " + game.getWm().getDescription().toUpperCase() + "</center></html>");
        guessL.setText("Guesses: " + game.guessesLeft); guessL.setForeground(new Color(70,215,110));
        warnL.setText("Warnings: " + game.warnings); warnL.setForeground(new Color(255,200,50));
        if (!msg.isEmpty()) {
            if (msg.contains("Digits and special symbols")) msgL.setForeground(new Color(255, 90, 90));
            else if (msg.contains("Invalid") || msg.contains("already")) msgL.setForeground(new Color(255, 200, 50));
            else msgL.setForeground(msg.contains("Good job") ? new Color(70, 215, 110) : new Color(100, 180, 255));
            msgL.setText(msg);
        }
        StringBuilder sb = new StringBuilder(); for(char c:game.avail) sb.append(c).append(" ");
        availL.setText(sb.toString().trim().toUpperCase()); hp.setData(game.totalGuessesUsed, game.wrong);
    }
    private void triggerFullBlackScreen(boolean win) {
        JPanel blackPanel = new JPanel(new GridBagLayout()); blackPanel.setBackground(Color.BLACK);
        GridBagConstraints gbc = new GridBagConstraints(); gbc.gridx = 0; gbc.gridy = GridBagConstraints.RELATIVE; gbc.insets = new Insets(15, 20, 15, 20); gbc.anchor = GridBagConstraints.CENTER;
        JLabel mainTitle = new JLabel(win ? "GAME OVER - YOU WIN" : "GAME OVER - YOU LOSE", 0);
        mainTitle.setFont(new Font("Impact", Font.PLAIN, 42)); mainTitle.setForeground(win ? new Color(0, 255, 100) : new Color(255, 0, 50)); blackPanel.add(mainTitle, gbc);
        JLabel revealLabel = new JLabel("THE WORD WAS: " + game.getWm().getWord().toUpperCase(), 0);
        revealLabel.setFont(new Font("Courier New", Font.BOLD, 28)); revealLabel.setForeground(new Color(255, 215, 0)); blackPanel.add(revealLabel, gbc);
        JLabel promptLabel = new JLabel("CLICK ANYWHERE ON THIS BLACK SCREEN TO PLAY AGAIN", 0);
        promptLabel.setFont(new Font("Arial", Font.BOLD, 12)); promptLabel.setForeground(Color.DARK_GRAY); blackPanel.add(promptLabel, gbc);
        blackPanel.addMouseListener(new java.awt.event.MouseAdapter() { public void mousePressed(java.awt.event.MouseEvent e) { reset(); } });
        cardContainer.add(blackPanel, "GAMEOVER"); mainLayout.show(cardContainer, "GAMEOVER");
    }
    public static void main(String[] args) { SwingUtilities.invokeLater(() -> new final_game().setVisible(true)); }
}