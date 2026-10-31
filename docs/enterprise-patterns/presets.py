"""presets.py -- every lesson's lab instances and Java snippets (PLAN.md sections C and D.4).

`earef.py` imports this module. LESSONS holds the eakit instances, one tuple per
lesson: (tag, mode, view, cfg, [(preset id, instance)]); an id that starts with
"exercise" is the exercise's instance, never a preset (PLAN section B). CC_JOBS
holds the lessons that reuse cckit (PLAN section D.5), run by ccrun.js through
the shipped cckit JavaScript. SNIPPETS holds every Java snippet in the plan,
verbatim; STUBS the declarations `earef.py --javac` compiles each one against.

Every snippet was written for these lessons; none is the book's. Every figure
below is a preset's input: illustrative unless PLAN section S.2 names it.
"""

S = {}  # snippet name -> Java text (one Python constant per snippet in content/)

# ------------------------------------------------------------ course 1

S["DUE_DAY"] = """\
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    int day = invoiceDay + 30;
    if (c.isGovernment()) {
        day = day + 15;
    }
    if (c.region() == Region.NORTH && c.years() > 5) {
        day = day + 10;
    }
    if (c.isRetail() || c.isOnline()) {
        if (invoiceDay > 25) {
            day = day + 5;
        }
    }
    if (day > 60 && !c.isGovernment()) {
        day = 60;
    }
    return day;
}"""

S["DUE_DAY_PLAIN"] = """\
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    return invoiceDay + 30;
}"""

S["LATE_FEE"] = """\
// Fee in cents for a late payment, with the agreed exceptions.
long lateFee(Account a, int daysLate) {
    long fee = 0;
    if (daysLate > 10) {
        fee = 500;
    }
    if (daysLate > 30 || a.isFlagged()) {
        fee = 2500;
    }
    if (a.isCharity() && daysLate < 60) {
        fee = 0;
    }
    if (a.isNew() && a.payments() == 0) {
        fee = fee / 2;
    }
    return fee;
}"""

S["RESPONSE_TIME"] = """\
// Times one request. Run it at each load you care about.
long responseMillis(Service service, Request request) {
    long start = System.nanoTime();
    service.handle(request);
    return (System.nanoTime() - start) / 1000000;
}"""

S["SERVERS_NEEDED"] = """\
// Servers needed for a target load, from two measured rates.
int serversNeeded(int firstTps, int extraTps, int targetTps) {
    if (extraTps <= 0 && firstTps < targetTps) {
        throw new IllegalArgumentException("more servers add nothing");
    }
    int servers = 1;
    int tps = firstTps;
    while (tps < targetTps) {
        servers = servers + 1;
        tps = tps + extraTps;
    }
    return servers;
}"""

S["RISING_TWICE"] = """\
// Web page: show a product, red if sales rose more than 10%.
void showProduct(Product p, Page page) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    page.write(p.name(), now, rising);
}

// Command line: the same report, for a script.
void printProduct(Product p, PrintStream out) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    out.println(p.name() + " " + now + (rising ? " *" : ""));
}"""

S["RISING_ONCE"] = """\
// Domain layer: the rule, in one place.
boolean isRising(Product p) {
    return p.salesThisMonth() * 100 > p.salesLastMonth() * 110;
}

// Presentation: the web page and the command line both ask.
void showProduct(Product p, Page page) {
    page.write(p.name(), p.salesThisMonth(), isRising(p));
}

void printProduct(Product p, PrintStream out) {
    String mark = isRising(p) ? " *" : "";
    out.println(p.name() + " " + p.salesThisMonth() + mark);
}"""

S["OVERDUE_TWICE"] = """\
// Report screen
void showInvoice(Invoice inv, Page page) {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    page.write(inv.number(), overdue);
}

// Nightly export
void exportInvoice(Invoice inv, Writer csv) throws IOException {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    csv.write(inv.number() + "," + overdue + "\\n");
}"""

S["SEPARATED_FINDER"] = """\
// Domain package: the interface the domain needs.
interface OrderFinder {
    Order find(long id);
}

// Domain package: Order uses only the interface.
class Order {
    private static OrderFinder finder;
    static void setFinder(OrderFinder f) { finder = f; }
    static Order load(long id) { return finder.find(id); }
}

// Mapper package: the implementation, which knows the SQL.
class OrderMapper implements OrderFinder {
    public Order find(long id) {
        // SELECT ... FROM orders WHERE id = ?
        return new Order();
    }
}"""

# ------------------------------------------------------------ course 2

S["TWO_SCRIPTS"] = """\
// Script for "place order".
void placeOrder(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    db.insertOrder(o.id(), total);
}

// Script for "quote price": the same discount, copied.
long quotePrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}"""

S["SHARED_SUBROUTINE"] = """\
// The discount, once, as a subroutine both scripts call.
long memberPrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}

void placeOrder(Order o) {
    db.insertOrder(o.id(), memberPrice(o));
}

long quotePrice(Order o) {
    return memberPrice(o);
}"""

S["SHIPPING_TWICE"] = """\
// Script for "check out".
void checkOut(Cart cart) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    db.insertOrder(cart.id(), cents + shipping);
}

// Script for "show basket".
void showBasket(Cart cart, Page page) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    page.write(cents, shipping);
}"""

S["PRICE_BY_KIND"] = """\
// One routine prices every kind of product.
long price(Product p, int qty) {
    long cents = p.unitCents() * qty;
    if (p.kind() == Kind.BOOK) {
        cents = cents - cents / 20;
    } else if (p.kind() == Kind.ALCOHOL) {
        cents = cents + cents / 5;
    } else if (p.kind() == Kind.FOOD && qty > 10) {
        cents = cents - cents / 10;
    }
    return cents;
}"""

S["PRICE_DELEGATED"] = """\
// Each kind of product carries its own rule; Product is the default.
class Product {
    long unitCents;
    long adjust(long cents, int qty) { return cents; }
    long price(int qty) { return adjust(unitCents * qty, qty); }
}
class Book extends Product {
    long adjust(long cents, int qty) { return cents - cents / 20; }
}
class Alcohol extends Product {
    long adjust(long cents, int qty) { return cents + cents / 5; }
}
class Food extends Product {
    long adjust(long cents, int qty) {
        if (qty > 10) { return cents - cents / 10; }
        return cents;
    }
}"""

S["SHIPPING_BY_METHOD"] = """\
// Shipping cost in cents, by method and weight.
long shippingCents(Parcel p) {
    if (p.method() == Method.POST) {
        return 300 + 50 * p.kilos();
    } else if (p.method() == Method.COURIER && p.kilos() > 20) {
        return 2500;
    } else if (p.method() == Method.COURIER) {
        return 1200;
    } else if (p.method() == Method.COLLECT || p.isStaff()) {
        return 0;
    }
    return 999;
}"""

S["TABLE_MODULE"] = """\
// One object for the whole invoice-line table, not one per row.
class InvoiceLines {
    private final RecordSet rows;

    InvoiceLines(RecordSet rows) {
        this.rows = rows;
    }

    long totalCents(long invoiceId) {
        long total = 0;
        for (Record r : rows.where("invoice_id", invoiceId)) {
            total = total + r.getLong("cents");
        }
        return total;
    }
}"""

S["ORDERS_TWICE"] = """\
// The web page and the nightly import both place orders.
void webPlace(Request req) {
    Order order = orders.fromForm(req);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}

void importPlace(Row row) {
    Order order = orders.fromRow(row);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}"""

S["ORDERS_SERVED"] = """\
// Each client builds its order, then asks the service to place it.
void webPlace(Request req) {
    service.placeOrder(orders.fromForm(req));
}

void importPlace(Row row) {
    service.placeOrder(orders.fromRow(row));
}

// In OrderService: the application logic, in one place.
void placeOrder(Order order) {
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}"""

S["CANCEL_TWICE"] = """\
void webCancel(Request req) {
    Order order = orders.find(req.param("id"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}

void phoneCancel(ApiCall call) {
    audit.record(call);
    Order order = orders.find(call.field("order"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}"""

S["DATE_RANGE_MUTABLE"] = """\
class DateRange {
    public LocalDate start;
    public LocalDate end;

    public void setEnd(LocalDate end) {
        this.end = end;
    }

    public boolean includes(LocalDate d) {
        return !d.isBefore(start) && !d.isAfter(end);
    }
}"""

S["DATE_RANGE_VALUE"] = """\
final class DateRange {
    private final LocalDate start;
    private final LocalDate end;

    DateRange(LocalDate start, LocalDate end) {
        this.start = start;
        this.end = end;
    }

    public boolean equals(Object o) {
        if (!(o instanceof DateRange)) { return false; }
        DateRange r = (DateRange) o;
        return start.equals(r.start) && end.equals(r.end);
    }

    public int hashCode() {
        return 31 * start.hashCode() + end.hashCode();
    }
}"""

S["QUANTITY_MUTABLE"] = """\
class Quantity {
    public int amount;
    public String unit;
    private final int max = 1000;

    public void add(int n) {
        amount = amount + n;
    }

    public String toString() {
        return amount + " " + unit;
    }

    int room() {
        return max - amount;
    }
}"""

S["REFUND_SPLIT"] = """\
// Refunds an order across the payments that paid for it, in
// proportion to each; Money does the splitting, this checks it.
List<Refund> refund(Money total, List<Payment> paid) {
    long[] weights = new long[paid.size()];
    for (int i = 0; i < weights.length; i++) {
        weights[i] = paid.get(i).amount().cents();
    }
    Money[] parts = total.splitBy(weights);
    Money sum = Money.zero(total.currency());
    List<Refund> out = new ArrayList<Refund>();
    for (int i = 0; i < parts.length; i++) {
        sum = sum.plus(parts[i]);
        out.add(new Refund(paid.get(i), parts[i]));
    }
    if (!sum.equals(total)) {
        throw new IllegalStateException("refund parts do not add up");
    }
    return out;
}"""

S["NULL_CHECKS"] = """\
String greeting(Customer c) {
    String name = "friend";
    if (c != null && c.name() != null) {
        name = c.name();
    }
    String plan = "basic";
    if (c != null && c.plan() != null) {
        plan = c.plan().title();
    }
    return "Dear " + name + ", your plan: " + plan;
}"""

S["GUEST_CUSTOMER"] = """\
// The finder returns a GuestCustomer instead of null.
class GuestCustomer extends Customer {
    String name() { return "friend"; }
    Plan plan() { return Plan.BASIC; }
}

String greeting(Customer c) {
    return "Dear " + c.name() + ", your plan: " + c.plan().title();
}"""

S["NULL_ADDRESS"] = """\
String label(Order o) {
    Address a = o.address();
    String city = "unknown";
    if (a != null && a.city() != null) {
        city = a.city();
    }
    if (a == null || a.postcode() == null) {
        return city;
    }
    return city + " " + a.postcode();
}"""

# ------------------------------------------------------------ course 3

S["PRICE_GATEWAY"] = """\
// All the SQL for the price table, in one class.
class PriceGateway {
    private final Connection db;

    PriceGateway(Connection db) {
        this.db = db;
    }

    long findCents(String sku) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT cents FROM price WHERE sku = ?");
        s.setString(1, sku);
        ResultSet rs = s.executeQuery();
        return rs.next() ? rs.getLong(1) : -1;
    }
}"""

S["ORDER_ROW"] = """\
// A gateway for one row of the orders table, and its finder.
class OrderRow {
    final long id;
    String status;

    OrderRow(long id, String status) {
        this.id = id;
        this.status = status;
    }

    static OrderRow find(Connection db, long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT status FROM orders WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        return rs.next() ? new OrderRow(id, rs.getString(1)) : null;
    }
}"""

S["ACCOUNT_RECORD"] = """\
// An Active Record: a row's data, its SQL and its domain logic.
class Account {
    private long id;
    private long balance;
    private long overdraft;

    static Account find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new Account();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }

    public boolean canWithdraw(long cents) {
        return balance + overdraft >= cents;
    }
}"""

S["ACCOUNT_ROW"] = """\
// A Row Data Gateway: the same row, with no domain logic.
class AccountRow {
    private long id;
    private long balance;
    private long overdraft;

    static AccountRow find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new AccountRow();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }
}"""

S["MEMBER_RECORD"] = """\
class Member {
    private long id;
    public String email;
    private int points;

    static Member find(Connection db, long id) throws SQLException {
        // SELECT email, points FROM member WHERE id = ?
        return new Member();
    }

    public void insert(Connection db) throws SQLException {
        // INSERT INTO member (email, points) VALUES (?, ?)
    }

    public int level() {
        return points / 1000;
    }
}"""

S["ACCOUNT_MAPPER"] = """\
// The mapper knows the table and the class; Account knows neither.
class AccountMapper {
    private final Connection db;

    AccountMapper(Connection db) {
        this.db = db;
    }

    Account find(long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT balance, overdraft FROM account WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        rs.next();
        return new Account(id, rs.getLong(1), rs.getLong(2));
    }
}"""

S["TWO_SOURCES"] = """\
// The same customer arrives from a table and from a message.
Customer fromRow(ResultSet rs) throws SQLException {
    String name = rs.getString("name");
    String postcode = rs.getString("postcode");
    long limit = rs.getLong("credit_limit");
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}

Customer fromMessage(Element msg) {
    String name = msg.getAttribute("name");
    String postcode = msg.getAttribute("post_code");
    long limit = Long.parseLong(msg.getAttribute("limit"));
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}"""

S["TWO_STEP"] = """\
// Step one, per source, holds the differences: to a logical record.
CustomerData fromRow(ResultSet rs) throws SQLException {
    return new CustomerData(rs.getString("name"),
        rs.getString("postcode"), rs.getLong("credit_limit"));
}

CustomerData fromMessage(Element msg) {
    return new CustomerData(msg.getAttribute("name"),
        msg.getAttribute("post_code"),
        Long.parseLong(msg.getAttribute("limit")));
}

// Step two, once, holds what they share: the record to the object.
Customer toCustomer(CustomerData d) {
    Customer c = new Customer(d.name.trim(), d.postcode.toUpperCase());
    c.setCreditLimit(d.limit);
    return c;
}"""

S["SHIPMENT_TWICE"] = """\
void toTable(Shipment s, PreparedStatement st) throws SQLException {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    st.setString(1, ref);
    st.setLong(2, grams);
    st.setString(3, to);
    st.executeUpdate();
}

void toMessage(Shipment s, Element msg) {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    msg.setAttribute("ref", ref);
    msg.setAttribute("grams", Long.toString(grams));
    msg.setAttribute("to", to);
}"""

S["SAVE_LINES_BATCH"] = """\
// Sends every line of an order to the database in one call.
void saveLines(Connection db, long orderId, List<Line> lines)
        throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "INSERT INTO line (order_id, sku, qty) VALUES (?, ?, ?)");
    for (Line line : lines) {
        s.setLong(1, orderId);
        s.setString(2, line.sku());
        s.setInt(3, line.qty());
        s.addBatch();
    }
    s.executeBatch();
}"""

# ------------------------------------------------------------ course 4

S["UNIT_OF_WORK"] = """\
// Remembers what changed; writes it all at commit. GONE: never written.
class UnitOfWork {
    enum Mark { NEW, DIRTY, REMOVED, GONE }
    private final Map<Entity, Mark> pending = new LinkedHashMap<>();
    void mark(Entity e, Mark asked) {
        Mark now = pending.get(e);
        boolean kept = now == Mark.NEW || now == Mark.REMOVED;
        boolean undone = now == Mark.NEW && asked == Mark.REMOVED;
        pending.put(e, undone ? Mark.GONE : kept ? now : asked);
    }
    void commit(Mapper db) {
        for (Map.Entry<Entity, Mark> p : pending.entrySet()) {
            switch (p.getValue()) {
                case NEW: db.insert(p.getKey()); break;
                case DIRTY: db.update(p.getKey()); break;
                case REMOVED: db.delete(p.getKey()); break;
            }
        }
    }
}"""

S["IDENTITY_MAP"] = """\
// One object per row: a second find returns the same object.
class CustomerMapper {
    private final Map<Long, Customer> loaded =
        new HashMap<Long, Customer>();

    Customer find(long id) throws SQLException {
        Customer c = loaded.get(id);
        if (c == null) {
            c = load(id);
            loaded.put(id, c);
        }
        return c;
    }

    private Customer load(long id) throws SQLException {
        // SELECT ... FROM customer WHERE id = ?
        return new Customer(id);
    }
}"""

S["LAZY_LINES"] = """\
// Loads an order's lines the first time something asks.
class Order {
    private final long id;
    private final LineMapper mapper;
    private final List<Line> lines = new ArrayList<>();
    private boolean linesLoaded = false;
    Order(long id, LineMapper mapper) {
        this.id = id;
        this.mapper = mapper;
    }

    List<Line> lines() throws SQLException {
        if (!linesLoaded) {
            lines.addAll(mapper.linesOf(id));
            linesLoaded = true;
        }
        return lines;
    }
}"""

S["SAVE_NEW_ORDER"] = """\
// Saves a new order and its lines: the parent row goes first.
void saveNew(Order order) throws SQLException {
    long orderId = keys.next("orders");
    insertOrder(orderId, order.customerId());
    for (Line line : order.lines()) {
        long lineId = keys.next("line");
        insertLine(lineId, orderId, line.sku(), line.qty());
    }
}"""

S["EMBEDDED_TERM"] = """\
// The lease's term has no table of its own: it is two columns.
Lease load(ResultSet rs) throws SQLException {
    DateRange term = new DateRange(
        rs.getDate("term_start").toLocalDate(),
        rs.getDate("term_end").toLocalDate());
    return new Lease(rs.getLong("id"), term);
}"""

S["THREAD_TEXT"] = """\
// Writes a reply thread into one text column, a line per post.
String toText(Post first) {
    StringBuilder out = new StringBuilder();
    Deque<Post> todo = new ArrayDeque<Post>();
    Deque<Integer> depths = new ArrayDeque<Integer>();
    todo.push(first);
    depths.push(0);
    while (!todo.isEmpty()) {
        Post p = todo.pop();
        int depth = depths.pop();
        out.append(depth).append(' ').append(p.id()).append('\\n');
        List<Post> replies = p.replies();
        for (int i = replies.size() - 1; i >= 0; i--) {
            todo.push(replies.get(i));
            depths.push(depth + 1);
        }
    }
    return out.toString();
}"""

S["SINGLE_TABLE_LOAD"] = """\
// One table for every kind of staff; a type column says which.
Staff load(ResultSet rs) throws SQLException {
    String type = rs.getString("type");
    long id = rs.getLong("id");
    String name = rs.getString("name");
    if (type.equals("C")) {
        return new Contractor(id, name, rs.getLong("day_rate"));
    }
    long salary = rs.getLong("salary");
    if (type.equals("M")) {
        return new Manager(id, name, salary, rs.getInt("reports"));
    }
    return new Employee(id, name, salary);
}"""

S["CLASS_TABLE_FIND"] = """\
// A manager's fields live in three tables, one per class.
static final String FIND_MANAGER =
    "SELECT p.name, e.salary, m.reports"
    + " FROM person p"
    + " JOIN employee e ON e.id = p.id"
    + " JOIN manager m ON m.id = p.id"
    + " WHERE p.id = ?";"""

S["HAND_MAPPING"] = """\
Member findMember(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(MEMBER_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Member m = new Member(id);
    m.email = rs.getString("email");
    m.city = rs.getString("city");
    return m;
}
Shop findShop(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(SHOP_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Shop p = new Shop(id);
    p.name = rs.getString("name");
    p.city = rs.getString("city");
    return p;
}"""

S["METADATA_FIND"] = """\
// The mapping held as data: each column and the field it fills.
static final String[][] MEMBER_MAP = {{"email", "email"},
                                      {"city", "city"}};

// One finder for every mapped class, which reads the map.
<T> T find(Class<T> type, String sql, String[][] map, long id)
        throws Exception {
    PreparedStatement s = db.prepareStatement(sql);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    T obj = type.getDeclaredConstructor(long.class).newInstance(id);
    for (String[] column : map) {
        Object value = rs.getObject(column[0]);
        type.getDeclaredField(column[1]).set(obj, value);
    }
    return obj;
}"""

S["INVOICE_FINDERS"] = """\
Invoice findInvoice(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(INVOICE_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Invoice i = new Invoice(id);
    i.total = rs.getLong("total");
    i.due = rs.getDate("due");
    return i;
}

Receipt findReceipt(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(RECEIPT_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Receipt r = new Receipt(id);
    r.paid = rs.getLong("paid");
    return r;
}"""

# ------------------------------------------------------------ course 5

S["CONCERT_MODEL"] = """\
// The model knows nothing of pages; the view asks the model.
class Concert {
    private final String act;
    private final String venue;
    Concert(String act, String venue) {
        this.act = act;
        this.venue = venue;
    }
    String act() { return act; }
    String venue() { return venue; }
}

class ConcertView {
    String render(Concert c) {
        return "<h1>" + escape(c.act()) + " at " + escape(c.venue())
            + "</h1>";
    }
}"""

S["CONCERT_PAGE"] = """\
// The page controller for one page: read input, choose a view.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    if (c == null) {
        res.forward("missing.jsp", null);
    } else if (c.isSoldOut()) {
        res.forward("waitlist.jsp", c);
    } else if (c.isSeated() && c.hasSeatMap()) {
        res.forward("seats.jsp", c);
    } else {
        res.forward("tickets.jsp", c);
    }
}"""

S["CONCERT_PAGE_SPLIT"] = """\
// The decisions move to a presentation helper; the model keeps its
// own predicates, and the controller only forwards.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    res.forward(helper.viewFor(c), c);
}"""

S["BOOKING_PAGE"] = """\
void doPost(Request req, Response res) throws IOException {
    Booking b = bookings.find(req.param("id"));
    String seats = req.param("seats");
    if (b == null || seats == null) {
        res.forward("error.jsp", null);
        return;
    }
    int n = Integer.parseInt(seats);
    if (n < 1 || n > 8) {
        res.forward("booking.jsp", b);
    } else if (b.isPaid() && !b.isRefundable()) {
        res.forward("locked.jsp", b);
    } else {
        b.setSeats(n);
        res.forward("confirm.jsp", b);
    }
}"""

S["PAGES_REPEAT"] = """\
void orderPage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("order.jsp", orders.find(req.param("id")));
}

void invoicePage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("invoice.jsp", invoices.find(req.param("id")));
}"""

S["PAGES_SUPERCLASS"] = """\
// A Layer Supertype runs the shared steps; each page adds its own.
abstract class SecurePage {
    void doGet(Request req, Response res) throws IOException {
        User u = sessions.user(req);
        if (u == null) { res.redirect("/login"); return; }
        audit.log(u, req.path());
        show(req, res);
    }
    abstract void show(Request req, Response res) throws IOException;
}
class OrderPage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("order.jsp", orders.find(req.param("id")));
    }
}
class InvoicePage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("invoice.jsp", invoices.find(req.param("id")));
    }
}"""

S["FRONT_HANDLER"] = """\
// One handler for every request; a command does each page's part.
void handle(Request req, Response res) throws IOException {
    Command c = commands.get(req.path());
    User u = sessions.user(req);
    if (u == null && c.needsLogin()) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    c.run(req, res);
}"""

S["REPORTS_REPEAT"] = """\
void salesReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.sales(req.param("month"));
    res.forward("sales.jsp", r.in(locale));
}

void stockReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.stock(req.param("depot"));
    res.forward("stock.jsp", r.in(locale));
}"""

S["TICKET_ROW"] = """\
// A row of the page, with its decisions inline.
String row(Ticket t) {
    String html = "<tr><td>" + escape(t.section()) + "</td>";
    if (t.seatsLeft() < 10 || t.isLastRelease()) {
        html = html + "<td class=\\"few\\">";
    } else {
        html = html + "<td>";
    }
    if (t.isResale() && !t.isLastRelease()) {
        html = html + "resale ";
    }
    return html + t.seatsLeft() + "</td></tr>";
}"""

S["TICKET_HELPER"] = """\
// The helper decides; the template only prints what it is given.
class TicketHelper {
    private final Ticket t;
    TicketHelper(Ticket t) { this.t = t; }
    boolean isFew() {
        return t.seatsLeft() < 10 || t.isLastRelease();
    }
    boolean showResale() {
        return t.isResale() && !t.isLastRelease();
    }
}"""

S["PRICE_CELL"] = """\
String cell(Item item, Locale locale) {
    String html = "<td>";
    if (item.onSale() && item.saleCents() < item.cents()) {
        html = html + "<s>" + money(item.cents(), locale) + "</s> ";
        html = html + money(item.saleCents(), locale);
    } else {
        html = html + money(item.cents(), locale);
    }
    if (item.stock() == 0 || item.isWithdrawn() || item.isRecalled()) {
        html = html + " (unavailable)";
    }
    return html + "</td>";
}"""

S["SECOND_STAGE"] = """\
// Stage one builds a logical screen; stage two turns it into HTML.
class Field {
    final String label;
    final String value;
    Field(String label, String value) {
        this.label = label;
        this.value = value;
    }
}

class HtmlRenderer {
    String render(List<Field> screen) {
        StringBuilder out = new StringBuilder("<dl>");
        for (Field f : screen) {
            out.append("<dt>").append(escape(f.label)).append("</dt>")
               .append("<dd>").append(escape(f.value)).append("</dd>");
        }
        return out.append("</dl>").toString();
    }
}"""

S["FLOW_REPEAT"] = """\
void afterAddress(Order o, Response res) throws IOException {
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}

void afterCart(Order o, Response res) throws IOException {
    if (!o.hasAddress()) { res.redirect("/address"); return; }
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}"""

S["NEXT_SCREEN"] = """\
// The flow in one place: which screen comes next.
String nextScreen(Order o) {
    if (!o.hasAddress()) { return "/address"; }
    if (o.needsCustomsForm()) { return "/customs"; }
    if (o.total() > LIMIT) { return "/approval"; }
    return "/payment";
}"""

S["CLAIM_FLOW"] = """\
void afterDetails(Claim c, Response res) throws IOException {
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}

void afterPhotos(Claim c, Response res) throws IOException {
    if (c.photos() == 0) { res.redirect("/photos"); return; }
    if (c.photosTooLarge()) { res.redirect("/resize"); return; }
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}"""

# ------------------------------------------------------------ course 6

S["COUNT_FILES"] = """\
// Two reads, and another session may commit between them.
int countFiles(Connection db) throws SQLException {
    int a = count(db, "locking");
    int b = count(db, "multiphase");
    return a + b;
}"""

S["TWO_CONTROLS"] = """\
class FileStore {
    private final Map<String, Integer> versions = new HashMap<>();
    private final Map<String, String> lockedBy = new HashMap<>();
    // Optimistic: detect a conflict when the session commits.
    boolean canCommit(String file, int versionWhenRead) {
        return versions.getOrDefault(file, 0) == versionWhenRead;
    }

    // Pessimistic: lock a file the session will edit before it is
    // loaded, so the session works on the latest version or not at all.
    boolean tryLoadForEdit(String file, String session) {
        String holder = lockedBy.get(file);
        if (holder != null && !holder.equals(session)) {
            return false;
        }
        lockedBy.put(file, session);
        return true;
    }
}"""

S["COUNT_SERIALIZABLE"] = """\
// Both counts inside one serializable transaction.
int countFiles(Connection db) throws SQLException {
    db.setAutoCommit(false);
    db.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
    int total = count(db, "locking") + count(db, "multiphase");
    db.commit();
    return total;
}"""

S["OPTIMISTIC_SAVE"] = """\
// Saves only if nobody has changed the row since it was read; false
// tells the caller to reload the invoice and let the user try again.
boolean trySave(Connection db, Invoice inv) throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "UPDATE invoice SET total = ?, version = version + 1"
        + " WHERE id = ? AND version = ?");
    s.setLong(1, inv.total());
    s.setLong(2, inv.id());
    s.setInt(3, inv.version());
    return s.executeUpdate() == 1;
}"""

S["GROUP_LOCK"] = """\
// Locks the order, not the line: one lock covers the group.
boolean tryEdit(Line line, String session) {
    String key = "order:" + line.orderId();
    String holder = owners.get(key);
    if (holder != null && !holder.equals(session)) {
        return false;
    }
    owners.put(key, session);
    return true;
}"""

S["STATELESS_HANDLER"] = """\
// Stateless: what a request needs arrives with it or is read
// from the database, so any server object can serve it.
class CartHandler {
    private final CartStore store;

    CartHandler(CartStore store) {
        this.store = store;
    }

    String handle(String cartId, String sku) {
        Cart cart = store.load(cartId);
        cart.add(sku);
        store.save(cart);
        return cart.summary();
    }
}"""

S["SERVER_SESSION"] = """\
// Server Session State: carts stay in server memory, keyed by
// the id the browser sends back with every request.
class Carts {
    private final Map<String, Cart> byId = new HashMap<String, Cart>();

    Cart forSession(String id) {
        Cart cart = byId.get(id);
        if (cart == null) {
            cart = new Cart();
            byId.put(id, cart);
        }
        return cart;
    }
}"""

# ------------------------------------------------------------ course 7

S["REMOTE_CUSTOMER"] = """\
// Each call on this interface crosses the network.
interface RemoteCustomer extends Remote {
    String name() throws RemoteException;
    String city() throws RemoteException;
    long creditCents() throws RemoteException;
}"""

S["CUSTOMER_FACADE"] = """\
// One remote call does the work of several local ones.
class CustomerFacade {
    private final CustomerRepository customers;

    CustomerFacade(CustomerRepository customers) {
        this.customers = customers;
    }

    void moveHouse(long id, String street, String city, String code) {
        Customer c = customers.find(id);
        c.address().setStreet(street);
        c.address().setCity(city);
        c.address().setPostcode(code);
        customers.save(c);
    }
}"""

S["ORDER_DTO"] = """\
// Everything the order screen shows, in one serializable bundle.
class OrderDto implements Serializable {
    long id;
    String customerName;
    String status;
    long totalCents;
    List<String> lineSummaries = new ArrayList<String>();
}"""

S["PLACE_ORDER_STACK"] = """\
// One request through every layer: the service runs the domain
// logic inside a unit of work, and the mappers do the SQL.
String placeOrder(String cartId) throws SQLException {
    UnitOfWork uow = new UnitOfWork();
    Cart cart = carts.find(cartId);
    Order order = cart.checkOut();
    uow.markNew(order);
    uow.markChanged(cart);
    uow.commit(mapper);
    return "Order " + order.number() + " placed";
}"""

S["ADDRESS_STUB"] = """\
// The interface the signup depends on, and a stub for its tests.
interface AddressCheck {
    boolean deliverable(String postcode);
}
class AddressCheckStub implements AddressCheck {
    public boolean deliverable(String postcode) {
        return !postcode.startsWith("ZZ");
    }
}

// The plugin: one switch on the environment, read once at startup.
class AddressChecks {
    static AddressCheck forEnvironment(String environment) {
        switch (environment) {
            case "test": return new AddressCheckStub();
            case "live": return new PostOfficeCheck();
            default: throw new IllegalArgumentException(environment);
        }
    }
}"""

SNIPPETS = S

# ------------------------------------------------------------ eakit lessons

SWORD_CAMEL = "swordfish, 1, 20; swordfish, 2, 35; camel, 1, 40; camel, 2, 50"

LESSONS = [
    ("1.2", "perf", "load", {}, [
        ("system-a-and-b", {"points": "a, 10, 500; a, 20, 500; b, 10, 200; b, 20, 2000", "users": "15"}),
        ("at-ten-users", {"points": "a, 10, 500; a, 20, 500; b, 10, 200; b, 20, 2000", "users": "10"}),
        ("exercise", {"points": "north, 5, 400; north, 25, 1400; south, 5, 900; south, 25, 1000", "users": "20"}),
    ]),
    ("1.3", "perf", "scale", {"unit": "server"}, [
        ("swordfish-and-camel", {"points": SWORD_CAMEL, "need": "40", "at": "5"}),
        ("need-120", {"points": SWORD_CAMEL, "need": "120", "at": "10"}),
        ("exercise", {"points": "heron, 1, 30; heron, 3, 54; stork, 1, 45; stork, 3, 57",
                      "need": "60", "at": "6"}),
    ]),
    ("2.3", "load", "instances", {}, [
        ("small-shop", {"tables": "customer, 200; orders, 1500; product, 120; line, 6000"}),
        ("one-big-table", {"tables": "reading, 250000; meter, 400"}),
        ("exercise", {"tables": "patient, 900; visit, 5400; doctor, 30; ward, 12"}),
    ]),
    ("2.6", "money", "allocate", {}, [
        ("nearest", {"amount": "5", "ratios": "70 30", "rule": "nearest"}),
        ("round-down", {"amount": "5", "ratios": "70 30", "rule": "down"}),
        ("rest-to-last", {"amount": "5", "ratios": "70 30", "rule": "last"}),
        ("allocator", {"amount": "5", "ratios": "70 30", "rule": "allocator"}),
        ("three-ways", {"amount": "100", "ratios": "1 1 1", "rule": "nearest"}),
        ("three-ways-allocated", {"amount": "100", "ratios": "1 1 1", "rule": "allocator"}),
        ("pennies-to-last", {"amount": "100", "ratios": "1 1 1 1 1 1 1", "rule": "last"}),
        ("exercise-nearest", {"amount": "100", "ratios": "1 1 1 1 1 1", "rule": "nearest"}),
        ("exercise-allocator", {"amount": "100", "ratios": "1 1 1 1 1 1", "rule": "allocator"}),
    ]),
    ("3.2", "load", "finds", {}, [
        ("fifty-or-one", {"wanted": "50", "broad": "200", "batch": "10", "latencyMs": "5", "rowMs": "0.1"}),
        ("local-database", {"wanted": "50", "broad": "200", "batch": "10", "latencyMs": "0.2", "rowMs": "0.1"}),
        ("exercise", {"wanted": "30", "broad": "600", "batch": "15", "latencyMs": "4", "rowMs": "0.05"}),
    ]),
    ("3.6", "remote", "calls", {}, [
        ("save-an-order", {"ops": "insert-order, 1; insert-lines, 12; update-stock, 12",
                           "latencyMs": "2", "workMs": "0.5"}),
        ("same-machine", {"ops": "insert-order, 1; insert-lines, 12; update-stock, 12",
                          "latencyMs": "0.1", "workMs": "0.5"}),
        ("exercise", {"ops": "insert-invoice, 1; insert-items, 40", "latencyMs": "3", "workMs": "0.2"}),
    ]),
    ("4.1", "uow", "commit", {}, [
        ("edit-an-order", {"script": "load, order7; change, order7; new, line1; new, line2; "
                                     "change, order7; delete, line2; load, customer3; change, line1"}),
        ("delete-loaded", {"script": "load, a1; load, a2; change, a1; delete, a2; change, a1"}),
        ("exercise", {"script": "load, invoice4; new, payment1; change, invoice4; change, invoice4; "
                                "load, account2; change, account2; new, note1; delete, note1; change, payment1"}),
    ]),
    ("4.2", "load", "identity", {}, [
        ("one-session", {"finds": "customer, 7; order, 31; customer, 7; order, 32; customer, 7; "
                                  "product, 5; product, 5"}),
        ("no-repeats", {"finds": "customer, 7; order, 31; product, 5"}),
        ("exercise", {"finds": "room, 12; guest, 3; room, 14; guest, 3; room, 12; guest, 9; guest, 3"}),
    ]),
    ("4.3", "load", "graph", {}, [
        ("orders-and-lines", {"parents": "o1, 3, yes; o2, 0, no; o3, 5, yes; o4, 2, no; o5, 4, yes",
                              "batch": "2"}),
        ("every-order-used", {"parents": "o1, 3, yes; o2, 0, yes; o3, 5, yes; o4, 2, yes; o5, 4, yes",
                              "batch": "2"}),
        ("exercise", {"parents": "a, 10, yes; b, 0, no; c, 2, no; d, 6, yes; e, 1, no; f, 3, yes",
                      "batch": "3"}),
    ]),
    ("4.4", "uow", "order", {}, [
        ("order-schema", {"keys": "orders, customer; line, orders; line, product; payment, orders",
                          "as": "line orders customer product payment"}),
        ("schema-only", {"keys": "orders, customer; line, orders; line, product; payment, orders"}),
        ("exercise", {"keys": "booking, guest; booking, room; room, hotel; charge, booking",
                      "as": "hotel guest booking room charge"}),
    ]),
    ("4.5", "load", "tree", {}, [
        ("thread", {"nodes": "start, -; ann, start; bo, ann; cy, ann; "
                             "dee, start; eli, dee; fay, eli; gus, eli"}),
        ("flat-thread", {"nodes": "start, -; ann, start; bo, start; cy, start"}),
        ("exercise", {"nodes": "root, -; a, root; b, a; c, b; d, c; e, root"}),
    ]),
    ("4.6", "inherit", "tables", {}, [
        ("staff", {"classes": "person, -, 3, no; employee, person, 2, yes; manager, employee, 2, yes; "
                              "contractor, person, 2, yes",
                   "load": "manager", "find": "person", "alter": "person"}),
        ("load-an-employee", {"classes": "person, -, 3, no; employee, person, 2, yes; manager, employee, 2, yes; "
                                         "contractor, person, 2, yes",
                              "load": "employee", "find": "employee", "alter": "manager"}),
        ("exercise", {"classes": "vehicle, -, 4, no; car, vehicle, 2, yes; van, vehicle, 3, yes; "
                                 "truck, vehicle, 5, yes",
                      "load": "van", "find": "vehicle", "alter": "vehicle"}),
    ]),
    ("4.7", "inherit", "tables", {}, [
        ("staff-find-person", {"classes": "person, -, 3, no; employee, person, 2, yes; "
                                          "manager, employee, 2, yes; contractor, person, 2, yes",
                               "load": "manager", "find": "person", "alter": "person"}),
        ("staff-find-employee", {"classes": "person, -, 3, no; employee, person, 2, yes; "
                                            "manager, employee, 2, yes; contractor, person, 2, yes",
                                 "load": "contractor", "find": "employee", "alter": "employee"}),
        ("exercise", {"classes": "account, -, 3, no; saving, account, 2, no; isa, saving, 1, yes; "
                                 "bond, saving, 2, yes; current, account, 2, yes",
                      "load": "bond", "find": "saving", "alter": "saving"}),
    ]),
    ("6.1", "lock", "reads", {}, [
        ("martin-and-david", {"items": "locking, 7, 9, before, insert; multiphase, 5, 8, after, insert"}),
        ("both-after", {"items": "locking, 7, 9, after, insert; multiphase, 5, 8, after, insert"}),
        ("both-before", {"items": "locking, 7, 9, before, insert; multiphase, 5, 8, before, insert"}),
        ("exercise", {"items": "cash, 400, 300, after, update; savings, 600, 700, before, update"}),
    ]),
    ("6.2", "lock", "timeline", {}, [
        ("no-control", {"events": "0, martin, read, design; 1, david, read, design; 5, david, edit, design; "
                                  "6, martin, edit, design; 8, david, commit, -; 10, martin, commit, -",
                        "scheme": "none"}),
        ("optimistic", {"events": "0, martin, read, design; 1, david, read, design; 5, david, edit, design; "
                                  "6, martin, edit, design; 8, david, commit, -; 10, martin, commit, -",
                        "scheme": "optimistic"}),
        ("pessimistic", {"events": "0, martin, read, design; 1, david, read, design; 5, david, edit, design; "
                                   "6, martin, edit, design; 8, david, commit, -; 10, martin, commit, -",
                         "scheme": "pessimistic"}),
        ("exercise", {"events": "0, ann, read, plan; 2, bo, read, plan; 3, ann, edit, plan; "
                                "4, bo, edit, plan; 9, bo, commit, -; 12, ann, commit, -",
                      "scheme": "optimistic"}),
        ("exercise-pessimistic", {"events": "0, ann, read, plan; 2, bo, read, plan; 3, ann, edit, plan; "
                                            "4, bo, edit, plan; 9, bo, commit, -; 12, ann, commit, -",
                                  "scheme": "pessimistic"}),
    ]),
    ("6.3", "lock", "reads", {}, [
        ("quarter-totals", {"items": "january, 400, 400, before, update; february, 300, 350, before, update; "
                                     "march, 0, 120, after, insert"}),
        ("only-a-new-row", {"items": "january, 400, 400, before, update; march, 0, 120, after, insert"}),
        ("exercise", {"items": "north, 12, 12, before, update; south, 8, 11, before, insert; "
                               "east, 5, 7, after, update"}),
    ]),
    ("6.4", "lock", "timeline", {}, [
        ("two-clerks", {"events": "0, kim, read, invoice; 1, lee, read, invoice; 2, lee, edit, invoice; "
                                  "3, lee, commit, -; 4, kim, edit, invoice; 20, kim, commit, -",
                        "scheme": "optimistic"}),
        ("inconsistent-read", {"events": "0, kim, read, discount; 0, kim, edit, quote; 1, lee, edit, discount; "
                                         "2, lee, commit, -; 6, kim, commit, -",
                               "scheme": "optimistic", "checkReads": "no"}),
        ("check-the-read", {"events": "0, kim, read, discount; 0, kim, edit, quote; 1, lee, edit, discount; "
                                      "2, lee, commit, -; 6, kim, commit, -",
                            "scheme": "optimistic", "checkReads": "yes"}),
        ("exercise", {"events": "0, ana, read, budget; 1, ben, read, budget; 2, ana, edit, budget; "
                                "5, ana, commit, -; 6, ben, edit, budget; 30, ben, commit, -; "
                                "31, cy, read, budget; 32, cy, edit, budget; 40, cy, commit, -",
                      "scheme": "optimistic"}),
    ]),
    ("6.5", "lock", "timeline", {}, [
        ("line-locks", {"events": "0, kim, edit, line1; 1, lee, edit, line2; 4, kim, commit, -; "
                                  "5, lee, commit, -",
                        "scheme": "pessimistic"}),
        ("order-lock", {"events": "0, kim, edit, line1; 1, lee, edit, line2; 4, kim, commit, -; "
                                  "5, lee, commit, -",
                        "scheme": "pessimistic", "groups": "line1=order9; line2=order9"}),
        ("optimistic-groups", {"events": "0, kim, edit, line1; 1, lee, edit, line2; 4, kim, commit, -; "
                                         "5, lee, commit, -",
                               "scheme": "optimistic", "groups": "line1=order9; line2=order9"}),
        ("exercise", {"events": "0, ann, edit, room1; 1, bo, edit, room2; 2, cy, edit, room3; "
                                "3, ann, commit, -; 7, bo, commit, -; 8, cy, commit, -",
                      "scheme": "pessimistic", "groups": "room1=floor1; room2=floor1; room3=floor2"}),
    ]),
    ("6.6", "session", "objects", {}, [
        ("hundred-users", {"users": "100", "serviceMs": "1000", "thinkMs": "10000"}),
        ("busier", {"users": "100", "serviceMs": "1000", "thinkMs": "2000"}),
        ("exercise", {"users": "250", "serviceMs": "400", "thinkMs": "20000"}),
    ]),
    ("6.7", "session", "state", {}, [
        ("a-megabyte", {"users": "100", "stateBytes": "1000000", "requests": "20", "idBytes": "32"}),
        ("a-small-cart", {"users": "100", "stateBytes": "2000", "requests": "20", "idBytes": "32"}),
        ("exercise", {"users": "5000", "stateBytes": "40000", "requests": "12", "idBytes": "32"}),
    ]),
    ("7.1", "remote", "boundary", {}, [
        ("by-class", {"calls": "screen, order, 20; order, customer, 10; order, product, 30; order, pricing, 15",
                      "nodes": "order=orders; customer=customers; product=catalog; pricing=pricing",
                      "remoteUs": "1000", "localUs": "1"}),
        ("one-process", {"calls": "screen, order, 20; order, customer, 10; order, product, 30; order, pricing, 15",
                         "nodes": "", "remoteUs": "1000", "localUs": "1"}),
        ("exercise", {"calls": "web, cart, 12; cart, stock, 8; cart, tax, 8; tax, rates, 16",
                      "nodes": "web=front; tax=back; rates=back", "remoteUs": "800", "localUs": "2"}),
    ]),
    ("7.2", "remote", "calls", {}, [
        ("move-house", {"ops": "moveHouse, 5; showCustomer, 6", "latencyMs": "20", "workMs": "0.5"}),
        ("on-a-fast-network", {"ops": "moveHouse, 5; showCustomer, 6", "latencyMs": "1", "workMs": "0.5"}),
        ("exercise", {"ops": "bookTrip, 8; cancelTrip, 3; showTrip, 9", "latencyMs": "15", "workMs": "1"}),
    ]),
    ("7.3", "remote", "payload", {}, [
        ("order-screen", {"fields": "id, 8, yes; customerName, 40, yes; status, 10, yes; "
                                    "totalCents, 8, yes; lines, 2000, yes; notes, 4000, no",
                          "latencyMs": "20", "bytesPerMs": "1000", "factor": "1"}),
        ("as-xml", {"fields": "id, 8, yes; customerName, 40, yes; status, 10, yes; "
                              "totalCents, 8, yes; lines, 2000, yes; notes, 4000, no",
                    "latencyMs": "20", "bytesPerMs": "1000", "factor": "3"}),
        ("exercise", {"fields": "name, 30, yes; email, 40, yes; photo, 60000, no; history, 9000, no",
                      "latencyMs": "10", "bytesPerMs": "2000", "factor": "1"}),
        ("exercise-shaped", {"fields": "name, 30, yes; email, 40, yes",
                             "latencyMs": "10", "bytesPerMs": "2000", "factor": "1"}),
    ]),
    ("7.4", "remote", "boundary", {}, [
        ("web-and-database", {"calls": "browser, page, 1; page, service, 2; service, domain, 40; "
                                       "domain, mapper, 25; mapper, database, 6",
                              "nodes": "browser=client; database=db",
                              "remoteUs": "2000", "localUs": "1"}),
        ("service-split-off", {"calls": "browser, page, 1; page, service, 2; service, domain, 40; "
                                        "domain, mapper, 25; mapper, database, 6",
                               "nodes": "browser=client; service=app; domain=app; mapper=app; database=db",
                               "remoteUs": "2000", "localUs": "1"}),
        ("domain-split-off", {"calls": "browser, page, 1; page, service, 2; service, domain, 40; "
                                       "domain, mapper, 25; mapper, database, 6",
                              "nodes": "browser=client; domain=app; mapper=app; database=db",
                              "remoteUs": "2000", "localUs": "1"}),
        ("exercise", {"calls": "app, facade, 3; facade, domain, 30; domain, mapper, 20; mapper, db, 4",
                      "nodes": "app=phone", "remoteUs": "50000", "localUs": "1"}),
    ]),
]

# ------------------------------------------------------------ cckit lessons (D.5)

B510 = {"bands": [5, 10]}


def code(i, view, name, **kw):
    j = {"id": i, "mode": "code", "view": view, "code": S[name], "snippet": name}
    if view == "complexity":
        j["opts"] = dict(B510)
    if view == "dupes":
        j["opts"] = {"min_run": 2}
    j.update(kw)
    return j


def deps(i, view, edges, changed=None):
    j = {"id": i, "mode": "deps", "view": view, "edges": edges}
    if changed:
        j["changed"] = changed
    return j


CC_JOBS = [
    code("1.1 due-day", "complexity", "DUE_DAY"),
    code("1.1 due-day-plain", "complexity", "DUE_DAY_PLAIN"),
    code("1.1 exercise", "complexity", "LATE_FEE"),
    code("1.4 rising-twice", "dupes", "RISING_TWICE"),
    code("1.4 rising-once", "dupes", "RISING_ONCE"),
    code("1.4 exercise", "dupes", "OVERDUE_TWICE"),
    deps("1.5 mapper-in-domain", "ripple", "screen, order; order, mapper; mapper, order; mapper, jdbc", "jdbc"),
    deps("1.5 separated", "ripple",
         "screen, order; order, finder; mapper, finder; mapper, order; mapper, jdbc; main, mapper", "jdbc"),
    deps("1.5 exercise", "ripple", "report, invoice; invoice, pdfwriter; pdfwriter, fontlib", "fontlib"),
    deps("1.5 exercise-after", "ripple",
         "report, invoice; pdfwriter, invoice; pdfwriter, fontlib; main, pdfwriter", "fontlib"),
    code("2.1 two-scripts", "dupes", "TWO_SCRIPTS"),
    code("2.1 shared-subroutine", "dupes", "SHARED_SUBROUTINE"),
    code("2.1 exercise", "dupes", "SHIPPING_TWICE"),
    code("2.2 price-by-kind", "complexity", "PRICE_BY_KIND"),
    code("2.2 price-delegated", "complexity", "PRICE_DELEGATED"),
    code("2.2 exercise", "complexity", "SHIPPING_BY_METHOD"),
    code("2.4 orders-twice", "dupes", "ORDERS_TWICE"),
    code("2.4 orders-served", "dupes", "ORDERS_SERVED"),
    code("2.4 exercise", "dupes", "CANCEL_TWICE"),
    code("2.5 mutable-range", "class", "DATE_RANGE_MUTABLE"),
    code("2.5 value-range", "class", "DATE_RANGE_VALUE"),
    code("2.5 exercise", "class", "QUANTITY_MUTABLE"),
    code("2.7 null-checks", "complexity", "NULL_CHECKS"),
    code("2.7 guest-customer", "complexity", "GUEST_CUSTOMER"),
    code("2.7 exercise", "complexity", "NULL_ADDRESS"),
    deps("3.1 sql-everywhere", "ripple",
         "cart, price-table; checkout, price-table; report, price-table; admin, price-table", "price-table"),
    deps("3.1 one-gateway", "ripple",
         "cart, pricegateway; checkout, pricegateway; report, pricegateway; admin, pricegateway; "
         "pricegateway, price-table", "price-table"),
    deps("3.1 exercise", "ripple",
         "signup, member-table; profile, member-table; mailer, member-table; profile, mailer", "member-table"),
    deps("3.1 exercise-after", "ripple",
         "signup, membergateway; profile, membergateway; mailer, membergateway; profile, mailer; "
         "membergateway, member-table", "member-table"),
    code("3.3 active-record", "class", "ACCOUNT_RECORD"),
    code("3.3 row-gateway", "class", "ACCOUNT_ROW"),
    code("3.3 exercise", "class", "MEMBER_RECORD"),
    deps("3.4 active-record", "ripple", "screen, account; report, account; account, jdbc", "jdbc"),
    deps("3.4 mapper", "ripple",
         "screen, account; report, account; mapper, account; mapper, jdbc; main, mapper", "jdbc"),
    deps("3.4 mapper-domain-change", "ripple",
         "screen, account; report, account; mapper, account; mapper, jdbc; main, mapper", "account"),
    deps("3.4 active-record-domain-change", "ripple", "screen, account; report, account; account, jdbc",
         "account"),
    deps("3.4 exercise", "ripple",
         "web, invoice; invoice, customer; invoicemapper, invoice; invoicemapper, jdbc; "
         "customermapper, customer; customermapper, jdbc; main, invoicemapper; main, customermapper", "jdbc"),
    code("3.5 two-sources", "dupes", "TWO_SOURCES"),
    code("3.5 two-step", "dupes", "TWO_STEP"),
    code("3.5 exercise", "dupes", "SHIPMENT_TWICE"),
    code("4.8 hand-mapping", "dupes", "HAND_MAPPING"),
    code("4.8 metadata-find", "dupes", "METADATA_FIND"),
    code("4.8 exercise", "dupes", "INVOICE_FINDERS"),
    deps("5.1 model-knows-html", "ripple", "concert, html; concertpage, concert; concertreport, concert", "html"),
    deps("5.1 separated", "ripple", "concertpage, concert; concertpage, html; concertreport, concert", "html"),
    deps("5.1 exercise", "ripple",
         "basket, widgets; checkoutpage, basket; basketapi, basket; checkoutpage, widgets", "widgets"),
    deps("5.1 exercise-after", "ripple", "checkoutpage, basket; basketapi, basket; checkoutpage, widgets", "widgets"),
    code("5.2 concert-page", "complexity", "CONCERT_PAGE"),
    code("5.2 concert-page-split", "complexity", "CONCERT_PAGE_SPLIT"),
    code("5.2 exercise", "complexity", "BOOKING_PAGE"),
    code("5.3 pages-repeat", "dupes", "PAGES_REPEAT"),
    code("5.3 page-superclass", "dupes", "PAGES_SUPERCLASS"),
    code("5.3 front-handler", "dupes", "FRONT_HANDLER"),
    code("5.3 exercise", "dupes", "REPORTS_REPEAT"),
    code("5.4 ticket-row", "complexity", "TICKET_ROW"),
    code("5.4 ticket-helper", "complexity", "TICKET_HELPER"),
    code("5.4 exercise", "complexity", "PRICE_CELL"),
    deps("5.5 one-step", "ripple",
         "concertpage, look; venuepage, look; tourpage, look; concertpage, concert; venuepage, venue", "look"),
    deps("5.5 two-step", "ripple",
         "concertpage, screen; venuepage, screen; tourpage, screen; renderer, screen; renderer, look; "
         "concertpage, concert; venuepage, venue", "look"),
    deps("5.5 exercise", "ripple",
         "home, screen; search, screen; account, screen; renderer, screen; renderer, look; "
         "printrenderer, screen; printrenderer, printlook", "screen"),
    code("5.6 flow-repeat", "dupes", "FLOW_REPEAT"),
    code("5.6 next-screen", "dupes", "NEXT_SCREEN"),
    code("5.6 exercise", "dupes", "CLAIM_FLOW"),
    deps("7.5 real-service", "ripple",
         "signup, postoffice; postoffice, network; signuptest, signup", "network"),
    deps("7.5 plugin-and-stub", "ripple",
         "signup, addresscheck; postofficecheck, addresscheck; postofficecheck, network; "
         "addresscheckstub, addresscheck; signuptest, signup; signuptest, addresscheckstub; "
         "main, postofficecheck", "network"),
    deps("7.5 exercise", "ripple",
         "invoice, ratesfeed; ratesfeed, http; invoicetest, invoice", "http"),
    deps("7.5 exercise-after", "ripple",
         "invoice, rates; httprates, rates; httprates, http; ratesstub, rates; "
         "invoicetest, invoice; invoicetest, ratesstub; main, httprates", "http"),
]
