namespace backend.Application.Interfaces
{
    public interface IQuotationService
    {
        Task<Quotation> GetQuotationAsync(string currencyFrom, string currencyTo);
    }
}